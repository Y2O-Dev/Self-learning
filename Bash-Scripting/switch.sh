#!/bin/bash

food="amala"

case "$food" in

"amala")
        echo "Amala is great"
        ;;
"fufu")
        echo "Fufu is good"
        ;;
*)
        echo "Not a food"
        ;;
esac