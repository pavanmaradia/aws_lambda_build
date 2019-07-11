"""
This is error module where all errors are listed
"""

ERRORS = {
    'BUILD_VALID_404001': {
        'message': 'Repository path does not exists'
    },
    'BUILD_VALID_404002': {
        'message': 'Interpreter path does not exists'
    },
    'BUILD_VALID_404003': {
        'message': 'Virtual Environment path does not exists'
    },
    'BUILD_VALID_404004': {
        'message': 'Configuration file does not exists'
    },
    'BUILD_VALID_400001': {
        'message': 'Currently we are only supports json files for lambda '
                   'configurations'
    },
    'BUILD_VALID_400002': {
        'message': 'Based on Interpreter path, site-package path could not '
                   'found.'
    },
    'BUILD_VALID_400003': {
        'message': 'Based on Virtual environment path, site-package path '
                   'could not found.'
    },
    'BUILD_VALID_400004': {
        'message': 'Configuration File is not json file'
    },
}
