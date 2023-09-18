#!/bin/bash

# Cmd Substitution is storing the output of a cmd execution in
# a variable: `` or $()

cur_dir=`pwd`
echo $cur_dir

cur_dir=$(pwd)
echo $cur_dir
