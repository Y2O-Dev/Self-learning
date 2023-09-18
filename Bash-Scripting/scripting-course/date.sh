#!/bin/bash
# calculate the number of days between two days

echo "This script estimate the number of days between two provided date"
sleep 4

read -p "Enter the first date (e.g Jan 1, 2023): " date1
read -p "Enter the second date (e.g July 1, 2023): " date2

time1=$(date -d "$date1" +%s)
time2=$(date -d "$date2" +%s)

diff=$(expr $time2 - $time1)
secondsinday=$(expr 24 \* 60 \* 60)

days=$(expr $diff / $secondsinday)

echo The difference between $date2 and $date1 is $days days 

remdays=$[365 - $days]

echo The year is left with $remdays days to wind up.

