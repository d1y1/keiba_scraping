#!/bin/bash
kill -9 `cat /var/log/save_pid.txt`
rm /var/log/save_pid.txt
cd /root/python
git pull origin master
nohup python3 index.py > /var/log/nohup.log &
echo $! > /var/log/save_pid.txt
