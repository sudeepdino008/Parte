#!/usr/bin/env python
import sys
import random
from random import randrange
import numpy
sys.path.append("..")
sys.path.append("../log")
from CommonUtils import CommonUtils
from InProcessor import InProcessor
from Log import Log

class PartIn(InProcessor):
    '''write the process methods for returning input in string form'''
    global log
    log = Log()
    #generally i, when not None, will be some number from 0 to n-1 incrementally
    def process(self,i=None):
        #example you wan the input file to be to be some number n(number if test case) and the next n lines have arbitrary numbers from 1 to 100
        size = randrange(1,1000) #select n
        s=str(size) 
        for j in range(size):
            randomValue = randrange(1,101)
            s=s+"\n"+str(randomValue)
        return s
        

