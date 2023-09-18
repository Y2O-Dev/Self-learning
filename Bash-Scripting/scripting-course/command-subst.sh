#!/bin/bash

echo "*************************************************************"
echo "Welcome $USER on $HOSTNAME"
echo "*************************************************************"

FREERAM=$(free -m | grep Mem | awk '{print $4}')

LOAD=`uptime | awk '{print $11}'`

ROOTFREE=`df -h | grep '/dev/sda3' | awk '{print $4}'`

echo "#############################################################"
echo "Available free RAM is $FREERAM MB"
echo "#############################################################"
echo "Current load average is $LOAD"
echo "#############################################################"
echo "Free root partition is $ROOTFREE"
