"""
This is a main run module
"""

import os
from argparse import ArgumentParser

from build_controller import BuildController

if __name__ == '__main__':
    PARSER = ArgumentParser()
    PARSER.add_argument(
        '-r', '--repo_path', type=str,
        help="Provide main repository path"
    )

    PARSER.add_argument(
        '-i', '--interpreter_path', type=str,
        help='Python interpreter path where site packages are stored'
    )

    PARSER.add_argument(
        '-v', '--virtualenv_path', type=str,
        help='If you used virtual environment then provide virtual env'
             'path'
    )

    PARSER.add_argument(
        '-c', '--configuration', type=str,
        help='Lambda Configuration file path'
    )

    PARSER.add_argument(
        '-l', '--lambda_directory', type=str,
        help='If there are any preference to create lambda in sepecific '
             'directory then provide Destination folder.'
    )

    ARGUMENTS = PARSER.parse_args()

    REPO_PATH = ARGUMENTS.repo_path
    INTERPRETER_PATH = ARGUMENTS.interpreter_path
    VIRTUAL_ENV_PATH = ARGUMENTS.virtualenv_path
    CONFIGURATION_PATH = ARGUMENTS.configuration
    #LAMBDA_DIRECTORY_PATH = ARGUMENTS.lambda_directory

    if REPO_PATH and (INTERPRETER_PATH or VIRTUAL_ENV_PATH) and CONFIGURATION_PATH:
        os.environ['REPO_PATH']= REPO_PATH
        if INTERPRETER_PATH:
            os.environ['INTERPRETER_PATH']= INTERPRETER_PATH
        else:
            os.environ['VIRTUAL_ENV_PATH']= VIRTUAL_ENV_PATH
        os.environ['CONFIGURATION_PATH']= CONFIGURATION_PATH
        #os.environ['LAMBDA_DIRECTORY_PATH]= LAMBDA_DIRECTORY_PATH

    print(BuildController().controller())
