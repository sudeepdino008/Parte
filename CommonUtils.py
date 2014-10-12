#!/usr/bin/env python
import datetime
import os
import numpy

class CommonUtils():
    @classmethod
    def writeToFile(self,string,fileName,directory='',mode='w'):
        '''Write string to fileName'''
        
        directory = os.path.join(directory,fileName)
        with open(directory,mode) as myFile:
            myFile.write(str(string))
         
    @classmethod
    def prependDate(self, string):
        return "+"*20+CommonUtils.returnDate()+"+"*20+"\n"+string
    
    @classmethod
    def returnDate(self):
        return datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

    @classmethod
    def postpendSeparator(self, string):
        return string+"\n"+"-"*70+"\n"

    @classmethod #return rabndom list with elements from 1 to n of n size
    def randomList(self,n):
        return numpy.random.permutation(list(xrange(1,n)))
