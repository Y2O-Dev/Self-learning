#!/bin/bash
# echo -n "Hello! $(basename $0) ! May I ask your name: "
# read
# echo "Hello $REPLY"

# read -p "What is your profession? " job
# echo "Ok, you are a $job. That's great!"

read -p "What is your profession? " 
echo "Ok, you are a $REPLY. That's great!"
# read -n1 -p "Press any key to exit: "

# Controlling the visibility of the entered text
read -sn1 -p "Press any key to quit: "
echo

exit 0
