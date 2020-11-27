#!/bin/sh
for var in 6001 6002 6003 6004 6005 6006 6007 6008
do
    echo "shut down the poot:$var"
    for i in `ps -ef |grep "gunicorn -w 4 -b 0.0.0.0:$var" |grep -v "grep" |awk '{print $2}'`;
    do 
         echo $i;
         kill -9 $i;
    done
done
