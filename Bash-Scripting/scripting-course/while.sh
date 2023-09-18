#!/bin/bash

# for loop runs for sequence, while loop runs for conditions; as long as a condition remain true
#counter=0

#while [ $counter -lt 5 ]; do
#  echo "Looping............$(( $counter ))"
#  echo "Value of counter is $counter."
#  counter=$(( $counter +1 ))
#  sleep 1
#done

#sleep 1
#echo "Out of the looooooooooooop"


while [ -n "$1" ]
do 
case "$1" in 
-a) echo "-a option used" ;;
-b) echo "-b option used" ;;
-c) echo "-c option used" ;;
*) echo "Option  $1 is not an option" ;;

esac
shift
done
