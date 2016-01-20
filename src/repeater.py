#!/usr/bin/env python

import sys

if len(sys.argv) == 1:
   print "y"
else:
   print sys.argv[1][-1:]
