#for loop
echo "Bash version ${BASH_VERSION}"
for i in {0..10..2}; do
     echo "Welcome $i times"
done
exit 200

#for i in {1..30..2}; do echo "Welcome $i times"; exit 300; done

#for (( c=1; c<=5; c++ ))
#do  
#   echo "Welcome $c times"
#done

# PRACTICAL USE CASES-1

#for file in `ls`; do
#  echo "Line count of $file is `cat $file | wc -l`"
#done

## PRACTICAL USE CASES-2

#for package in $(cat install-package.txt)
#do
#  sudo apt install -y $package
#done

## PRACTICAL USE CASES-3

#for server in $(cat server.txt)
#do
#  ssh $server "uptime"
#done
