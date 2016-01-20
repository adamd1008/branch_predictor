#!/usr/bin/env python

import sys

if len(sys.argv) == 1:
   print "n"
else:
   if sys.argv[1][-1:] == "y":
      print "n"
   else:
      print "y"
