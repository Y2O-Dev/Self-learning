#!/bin/bash

a=20
read -p "Enter te second value >= 25: " b

if [ $a -lt 100 -a $b -gt 25 ]
then
    echo "$a is less than 100, while $b is geater than 25"
else
    echo "One of the condition is false"
fi

if [ $a -eq 100 -o $b -gt 25 ]
then
    echo "$a is equal 100, while $b is geater than 25"
else
    echo "One of the condition is false"
fi