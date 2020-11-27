#!/bin/sh
source venv/bin/activate
for var in 6001 6002 6003 6004 6005 6006 6007 6008
do
    nohup gunicorn -w 4 -b 0.0.0.0:$var main_flask:app --timeout 200 >> log/$var.out &
done
