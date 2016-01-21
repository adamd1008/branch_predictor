#!/usr/bin/env python

import sys

if len(sys.argv) == 1:
   print "y"
elif len(sys.argv[1]) == 1:
   print sys.argv[1][-1:]
else:
   l = len(sys.argv[1])
   
   if sys.argv[1][l - 2:l - 1] == sys.argv[1][-1:]:
      print sys.argv[1][-1:]
   else:
      if sys.argv[1][-1:] == "y":
         print "n"
      else:
         print "y"
