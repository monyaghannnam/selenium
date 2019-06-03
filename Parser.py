import argparse

class Parser:

    """class to make it easy to write auser friendly command-line interfaces
    """
    def __init__(self):
         parser = self.create_parser()
         parser = self.add_argument(parser)
         self.args = self.parse_arguments(parser)
          

    def create_parser(self):
        """create ArgumentParser object 
           :Return => ArgumentParser object.
        """ 
        parser = argparse.ArgumentParser(description='convert from xml to excel sheet')
        return parser

    def add_argument(self,parser):
        """tells the argument parser how to take string and turn them into objects
        :param1 parser => ArgumentParser object
        :type parser => ArgumentParser object
        :Return add_argument => ArgumentParser object.
        """
        parser.add_argument('-c','--csv',type=str,help='name of csv file')
        return parser

    def parse_arguments(self,parser):
        """convert each argument to appropriate data type
        :param1 parser => ArgumentParser object
        :type parser => ArgumentParser object
        :Return parse_arguments => ArgumentParser object.
        """
        return parser.parse_args()

    def get_args(self):
        """return instance of class argparse.The values returned by parsing will be stored 
           as attributes in this instance
        :Return get_args => instance of class argparse.Namespace
        """
        return self.args