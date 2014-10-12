#!/usr/bin/env python
import sys
import datetime
import argparse
sys.path.append("..")
sys.path.append("../log")
sys.path.append("../output")
sys.path.append("../input")
from Log import Log
from PartOut import PartOut
from PartIn import PartIn
from CommonUtils import CommonUtils
from threading import Thread
from time import sleep


class Parte():
    '''code to use input and output python code to write input, get output, compare them and display'''

    global log
    log = Log()

    def __init__(self, fileName, stopOnNo, np):
        self.partIn = PartIn()
        self.fileName = fileName.split('.')[0] #remove the .X part
        self.testFileName = self.fileName+"_test"
        self.partOut1 = PartOut(fileName)
        self.partOut2 = PartOut(self.testFileName+".cpp")
        self.stopOnNo = stopOnNo     #parameter determining to stop at a unsuccessful match
        self.noOutOnSuccess = np      #do not output anything in case of success


    def run(self, i=None):
        output = ''
        inputString = self.partIn.input(i)
        thread1 = Thread(target=self.partOut1.process, args=(inputString, ))
        thread2 = Thread(target=self.partOut2.process, args=(inputString, ))
        self.executeThreads(thread1, thread2)
        out1 = self.partOut1.returnOutput()
        out2 = self.partOut2.returnOutput()

        output = 'input:\n'+inputString+'\noutput1:\n'+out1+'\noutput2:\n'+out2+'\n'
        if out1!=out2:
            log.warning(output+'Error!')
            return False
        else:
            if not self.noOutOnSuccess:
                log.success(output+'Success!')
            return True
    
    def executeThreads(self, *threads):
        [x.start() for x in threads]
        [x.join() for x in threads]

    #for multiple runs on random input(no i)
    def multipleRun(self, n):
        for i in range(0,n):
            log.display('.'*6+'run-'+str(i+1)+'.'*6)
            if not self.run(i) and self.stopOnNo:
                return


class CliHandler():
    def main(self):
        parser = argparse.ArgumentParser(description='This is a testing module designed especially for competitive programming.')
        parser.add_argument('-i','--input',help='The input file name',required=True)
        parser.add_argument('-r', help='conduct a single run test', action='store_true')
        parser.add_argument('-m', '--multipleRun', help='conduct multiple run tests')
        parser.add_argument('-s', help='stop when output do not match', action='store_true')
        parser.add_argument('-np', help='No Print. Do not print the output messages which are successful', action='store_true')
        args = parser.parse_args()

        fileName = args.input
        ob = Parte(fileName, args.s, args.np)
        if args.multipleRun!=None:
            ob.multipleRun(int(args.multipleRun))
        else: #default option is ob.run()
            ob.run()

        

ob = CliHandler()
ob.main()
