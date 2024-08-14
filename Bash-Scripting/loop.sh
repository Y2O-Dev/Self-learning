#!/bin/bash
#set -vx

count=15

# while [ $count -le 10 ]; do
#     echo "$count. I'm loving \$BASH, thanks to Adam"
#     count=`expr $count + 1`
# done

# until [ $count -le 10 ]; do
#     echo "$count. I'm loving \$BASH, thanks to Adam"
#     count=`expr $count - 1`
# done

# for i in 1 2 3 4 5 
# do
#     echo "$i I am learning \$BASH"

#     if [ $i -eq 3 ]; then
#         echo "I'm out of the loop"
#         break
#     fi
# done

# for i in 1 2 3 4 5 
# do
#     echo "$i I am learning Python"

#     if [ $i -eq 3 ]; then
#         echo "I'll skip this"
#         continue
#     fi
# done

for i in $(seq 1 10)
do
    echo "$i I am learning Python"

    if [ $i -eq 3 ]; then
        continue
    fi
done
