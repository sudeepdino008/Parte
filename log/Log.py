import abc
import sys
import os
sys.path.append("..")

from CommonUtils import CommonUtils
from Colors import Colors

class Log():
    '''for outputting messages with appropriate colors'''
    
    def debug(self, string):
        print Colors.OKBLUE+string+Colors.ENDC

    def error(self,string):
        print Colors.FAIL+string+Colors.ENDC

    def warning(self,string):
        print Colors.WARNING+string+Colors.ENDC

    def display(self,string):
        print Colors.NORMAL+string+Colors.ENDC
        
    def success(self,string):
        print Colors.OKGREEN+string+Colors.ENDC
