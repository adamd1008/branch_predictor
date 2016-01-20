#!/usr/bin/env python

import sys
import subprocess32 as subprocess
import string
import random

class Test:
   def __init__(self, testString, desc):
      self.testString = testString
      self.desc = desc

   @classmethod
   def parse(cls, line):
      splitLine = string.split(line, ",")
      return cls(splitLine[0], splitLine[1])

class Predictor:
   def __init__(self, name, command):
      self.name = name
      self.command = command
      self.hit = 0
      self.miss = 0
   
   @classmethod
   def parse(cls, line):
      splitLine = string.split(line, ",")
      return cls(splitLine[0], splitLine[1])

if __name__ == "__main__":
   predictorFile = open("predictors.txt", "r")
   predictorList = predictorFile.read().splitlines()
   predictorFile.close()
   
   predictors = list()
   
   for predictor in predictorList:
      predictors.append(Predictor.parse(predictor))
   
   testFile = open("tests.txt", "r")
   testList = testFile.read().splitlines()
   testFile.close()
   
   tests = list()
   
   for test in testList:
      tests.append(Test.parse(test))
   
   # Now run the simulation!
   
   for predictor in predictors:
      sys.stdout.write("********\n\nPredictor \"" + predictor.name + "\"\n\n")
      disqualified = False
      
      for test in tests:
         hits = 0
         misses = 0
         
         if disqualified:
            break
         
         sys.stdout.write("* Test \"" + test.desc + "\"\n    ")
         
         for i in range(0, 72):
            history = test.testString[:i]
            action = "y"
            
            if len(history) == 0:
               p = subprocess.Popen(predictor.command,
                                    shell = True, stdout = subprocess.PIPE)
               
               try:
                  p.wait(timeout = 1)
               except subprocess.TimeoutExpired:
                  p.kill()
                  disqualified = True
               else:
                  action = p.stdout.read()[0]
            else:
               p = subprocess.Popen(predictor.command + " " + history,
                                    shell = True, stdout = subprocess.PIPE)
               
               try:
                  p.wait(timeout = 1)
               except subprocess.TimeoutExpired:
                  p.kill()
               else:
                  action = p.stdout.read()[0]
            
            if action != "y" and action != "n":
               disqualified = True
            
            if disqualified:
               sys.stdout.write("! Disqualified\n\n")
               break
            
            if action == test.testString[i]:
               hits += 1
               predictor.hit += 1
               sys.stdout.write("+")
            else:
               misses += 1
               predictor.miss += 1
               sys.stdout.write("-")
         
         if not disqualified:
            sys.stdout.write(" | result: " + str(hits) + "/" + str(hits + misses) + "\n")
      
      sys.stdout.write("\nTotal for \"" + predictor.name + "\": " + str(predictor.hit) + "/" + str(predictor.hit + predictor.miss) + " " + str(float(predictor.hit) / float(predictor.hit + predictor.miss) * 100) + "%\n\n")
