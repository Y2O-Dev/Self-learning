#!/bin/bash
#set -vx

count=15

# while [ $count -le 10 ]; do
#     echo "$count. I'm loving \$BASH, thanks to Adam"
#     count=`expr $count + 1`
# done

until [ $count -le 10 ]; do
    echo "$count. I'm loving \$BASH, thanks to Adam"
    count=`expr $count - 1`
done

for i in 1 2 3 4 5 
do
    echo "$i I am learning \$BASH"

    if [ $i -eq 4 ]; then
        break
done