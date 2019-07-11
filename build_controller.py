"""
Build Controller module which controls lambda build
"""

from validation.validate_paths import ValidatePaths


class BuildController(object):
    """
    This is a build controller class
    """

    def __init__(self):
        """
        Initialize the controller object
        """

        self.response = None

    def controller(self):
        """
        This is main controller
        :return:
        """

        # validate all paths
        self.response = ValidatePaths().controller()
        if self.response.get('status') is False:
            return self.response

        # create __lambda__ folders


        return self.response
