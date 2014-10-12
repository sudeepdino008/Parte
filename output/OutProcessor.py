#!/usr/bin/env python
import abc
import sys
sys.path.append("..")

from CommonUtils import CommonUtils

class OutProcessor():
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        self.output = ""
        self.fileName = ""
        
    @abc.abstractmethod
    def process(self):
        '''code for generating output from input file'''
        pass

    def returnOutput(self):
        return self.output
