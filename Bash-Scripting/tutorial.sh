#!/bin/bash

# To declare a fxn, 3 ways: 
function ip {
	echo "Here is a shell function"
 	`ip addr`
}

ip

name () {
echo "Hello!"
}


name
