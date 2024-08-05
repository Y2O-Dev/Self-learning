#!/bin/bash 

echo "The name of this file is $0"

var1=4
var2=16

prime=`expr $var2 % $var1`

echo $prime

if [ $prime -le 0 ]; then
    echo "$var2 is an even number"
else
    echo "$var2 is a prime number"
fi

if [ $var1 -gt $var2 ]; then
    echo "$var1 is greater than $var2"
else
    echo "$var1 is less than $var2"
fi

a="YAKUB"
b="DevOps"

if [ $a = $b ]; then
    echo "$a equals $b"
else
    echo "As strings, $a does not equals $b"

fi

if [ -z $a ]; then
    echo "-n $a is an empty string"
else
    echo "-n $a is'nt empty"
fi


# File Operators
file="/home/y2o/Self-learning/Bash-Scripting/tutorial.sh"

if [ -r $file ]
then
    echo "File has read access"
else
    echo "File does not have read access"
fi

if [ -w $file ]
then
    echo "File has write access"
else
    echo "File does not have write access"
fi

if [ -x $file ]
then
    echo "File has execute access"
else
    echo "File does not have execute access"
fi

if [ -e $file ]
then
    echo "File exist"
else
    echo "File does not exist"
fi

if [ -f $file ]
then
    echo "This is a normal file"
else
    echo "This is not a file"
fi

if [ -d $file ]
then
    echo "File is a directory"
else
    echo "File is not a directory"
fi

if [ -s $file ]
then
    echo "File has content"
else
    echo "File does not have any cotent"
fi

# ELIF
x=2
y=20

if [ $x -gt $y ]; then
    echo "$x is greater than $y"

elif [ $x == $y ]; then
    echo "Both $x and $y are equal"

else
    echo "$x is less than $y"
fi