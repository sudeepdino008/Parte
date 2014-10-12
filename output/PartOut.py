#!/usr/bin/env python
import sys
import os
import subprocess
sys.path.append("..")
sys.path.append("../log")
from Log import Log
from OutProcessor import OutProcessor

class PartOut(OutProcessor):
    '''code to take input.in file and write output to the log files'''
    inputDir = "../code"
    global log
    log = Log()

    def __init__(self, fileName):
        super(self.__class__ , self).__init__()
        self.fileName = fileName

    def process(self, inputString):
        os.chdir(self.inputDir)
        outputFile = self.fileName.split('.')[0] #remove the .X part
        subprocess.call(["g++", self.fileName, "-o", outputFile])
        p = subprocess.Popen(["./"+outputFile] , stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        
        self.output, err = p.communicate(input=inputString)
        if err!=None and err!='':
            log.error('Some error in compilation')
            exit(0)
        return self.output
