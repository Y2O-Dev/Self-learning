#!/usr/bin/env python

# import prime

# result = prime.checkIfPrime(13)
# print(result)

#A System Information Gathering Script
import subprocess

#Command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print ("Gathering system information with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])


#Command 2
def disk_func():
    top = "top"
    diskspace_arg = "-h"
    print ("Gathering diskspace information %s command:\n" % top)
    subprocess.call([top])

def alias_func():
    alias = "alias"
    subprocess.call([alias])

#Main function that call other functions
def main():
    uname_func()
    disk_func()
    alias_func()
    
main()