#!/bin/bash

if [ `../../utils/c_c++/random/urandom -d1u` -ge 128 ]; then
   echo "y"
else
   echo "n"
fi
