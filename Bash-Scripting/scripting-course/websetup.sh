#!/bin/bash

# Installing Dependencies
echo "################################################"
echo "Installing Packages"
echo "################################################"

sudo apt install wget unzip apache2 
echo 

# Start & Enable Services
echo "################################################"
echo "Start & Enable Services"
echo "################################################"

sudo systemctl start apache2
sudo systemctl enable apache2
echo

#Creating a Temp Directory
echo "################################################"
echo "Start Artifact Deployment"
echo "################################################"

mkdir -p /tmp/webfiles
cd /tmp/webfiles
echo

wget https://www.tooplate.com/zip-templates/2098_health.zip
unzip 2098_health.zip
sudo cp -r 2098_health.zip/* /var/www/html/

#Bounce Service
echo "################################################"
echo "Restarting apache2 Service"
echo "################################################"

sudo systemctl restart apache2
echo

#Clean up
echo "################################################"
echo "Removing Temporary Files"
echo "################################################"

rm -rf /tmp/webfiles