"""
Validate path module will validate all paths
"""

import os
from glob import glob
from json import load
from pathlib import Path
from platform import platform

from errors import ERRORS


class ValidatePaths(object):
    """
    This class will validate all the build related path like,
    repository_path: main repository path from where all files will be
                     collected and packed
    interpreter_path: validate python interpreter path
    virtualenv_path: if user used virtualenv then require virtualenv path so
                     all third-party library would be packed from there
    config_path: validation of configuration json file from where lambda
                 will generated
    """

    def __init__(self):
        """
        Initialize validation object
        """
        self.response = dict()
        self.paths = dict()
        self.validations = {
            'validate_path': self.validate_path,
            'validate_file_type': self.validate_file_type,
            'validate_site_packages': self.validate_site_packages,
            'validate_configuration_file': self.validate_configuration_file
        }

    def controller(self):
        """
        Controls validation process
        """
        self.parse_paths_form_env()
        for method_name, method in self.validations.items():
            method()

        return self.response

    def parse_paths_form_env(self):
        """
        Parse all paths from the environment
        """
        self.paths = {
            'Repository': os.getenv('REPO_PATH'),
            'Interpreter': os.getenv('INTERPRETER_PATH'),
            'Virtualenv': os.getenv('VIRTUAL_ENV_PATH'),
            'Configuration': os.getenv('CONFIGURATION_PATH')
        }

    def validate_path(self):
        """
        Validate all paths
        """
        errors = {
            'Repository': 'BUILD_VALID_404001',
            'Interpreter': 'BUILD_VALID_404002',
            'Virtualenv': 'BUILD_VALID_404003',
            'Configuration': 'BUILD_VALID_404004',
        }

        for _path_type, path in self.paths.items():
            if path is None:
                print(_path_type,"not set...continuing with virtualenv")
                continue
            elif not os.path.exists(path):
                self.response = {
                    'status': False,
                    'message': ERRORS.get(errors.get(_path_type))
                }
                return

        self.response = {'status': True}

    def validate_file_type(self):
        """
        Validate configuration file type
        """

        extension = Path(self.paths.get('Configuration')).suffix
        if extension.lower() == '.json':
            self.response = {'status': True}
        else:
            self.response = {
                'status': False,
                'message': ERRORS.get('BUILD_VALID_400001')
            }

    def validate_site_packages(self):
        """
        Validate site packages location
        """

        _python_path = self.paths.get('Interpreter')
        is_virtual_env = False
        if self.paths.get('Virtualenv'):
            _python_path = self.paths.get('Virtualenv')
            is_virtual_env = True

        lib_path = ''
        if platform().startswith('Darwin'):
            lib_path = os.path.join(
                _python_path, 'lib', 'python*'
            )
        elif platform().startswith('Windows'):
            lib_path = os.path.join(
                _python_path, 'lib', 'site-packages*'
            )

        version_path = glob(lib_path)
        if not version_path:
            error = 'BUILD_VALID_400002'
            if is_virtual_env:
                error = 'BUILD_VALID_400003'

            self.response = {
                'status': False,
                'message': ERRORS.get(error)
            }

    def validate_configuration_file(self):
        """
        Validate configuration path
        """

        try:
            with open(self.paths.get('Configuration'), 'r') as file:
                load(file)
            self.response = {'status': True}
        except:
            self.response = {
                'status': False,
                'error': ERRORS.get('BUILD_VALID_400004')
            }
