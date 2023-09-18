#!/bin/bash

 #if loop
read -p "Enter any number: "
if [ $REPLY -gt 20 ]
then
    sleep 2
    echo  "The value enter is more than 20"
    echo -e "Today's date is: `date` \n" 
    exit 200
else
	echo "The value entered is less than 20"
    echo -e "This laptop has been awake for about: `uptime`\n" 
#    exit 207
fi

value=`ip addr | grep -v link/loopback | grep -ic link`
if [ $value -eq 1 ]; then
  echo -e "1 active network interphase found. \n"
  
elif [ $value -gt 1 ]; then
  echo -e "Multiple active interphases found. \n"
  
else
  echo  -e "No active interphase found. \n"
fi


