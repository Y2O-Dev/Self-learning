#!/bin/bash
# set -vx
echo "HELLO YUSUF YO"


var1="yakub"
echo "My name is $var1"

echo $0
echo $1 $2 $3 $4 $5 $6 $7
echo $$
echo $?
echo $#
shift
echo "red yellow" 

echo $#

num1=49
num2=18

add=`expr $num1 + $num2`
echo $add

mul=`expr $num1 \* $num2`
echo $mul

mod=`expr $num1 % $num2`
echo $mod