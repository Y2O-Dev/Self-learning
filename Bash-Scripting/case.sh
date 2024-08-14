#!/bin/bash
shopt -s extglob

# read -p "Enter Yes/No: " choice

# case "$choice" in

# y|yes|Yes|YES|Y)
#         echo "You entered $choice as Yes"
#         ;;
# n|no|No|NO|N)
#         echo "You entered $choice as No"
#         ;;
# *)
#         echo "Enter a valid option"
#         ;;
# esac


#!/bin/bash

# read -p "Enter a number between 0 and 9: " REPLY

# case "$REPLY" in
#     0|1)
#         echo "Your response is $REPLY and it's a binary number" ;;
#     2|3|4|5|6|7|8|9)
#         echo "Your response is $REPLY but it's not a binary number" ;;
#     *)
#         echo "$REPLY you entered is a wrong number, try again" ;;
# esac


read -p "Enter a number between 0 and 1:  "

case "$REPLY" in

0|1)
   echo "Your respose is $REPLY and its a binary number" ;;

+([2-9]))
   echo "Your respose is $REPLY but its not a binary number" ;;

*)
   echo "$REPLY you entered is a wrong number, try again" ;;

esac