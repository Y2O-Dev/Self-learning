#!/bin/bash

echo "Testing nohup command with infinite while loop"
var=0
while [ $var > 0 ]; do
    # Your commands go here
    echo "$var This is an infinite loop. Press [CTRL+C] to stop."
    sleep 1  # Pause for 1 second to make the output more readable
    var=`expr $var + 1`
done
