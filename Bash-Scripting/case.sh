#!/bin/bash

read -p "Enter Yes/No: " choice

case "$choice" in

y|yes|Yes|YES|Y)
        echo "You entered $choice as Yes"
        ;;
n|no|No|NO|N)
        echo "You entered $choice as No"
        ;;
*)
        echo "Enter a valid option"
        ;;
esac