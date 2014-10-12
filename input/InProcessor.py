#!/usr/bin/env python
import abc
import sys
sys.path.append("..")

from CommonUtils import CommonUtils

class InProcessor():
    __metaclass__ = abc.ABCMeta
    inputString = ''

    @abc.abstractmethod
    def process(self):
        '''will be used for random data generated within the implemented process or manual input through if else or switch'''
        pass
    
    def randInput(self):
        self.inputString = self.process()
        return self.inputString
        
    def manualInput(self, i):
        self.inputString = self.process(i)
        return self.inputString
        
    def input(self, i=None, inputFile="input.in"):
        if i==None:
            return self.randInput()
        else:
            return self.manualInput(i)

    def returnInput(self):
        return self.inputString
