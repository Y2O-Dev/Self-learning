#!/bin/bash

echo "The Uptime of the system is:"
uptime
echo "######################################"

echo "Memory utilization"
free -m
echo "######################################"

echo "Disk utilization"
df -h
echo "######################################" 
