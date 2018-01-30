#!/bin/bash
killall -9 python3\ index.py
cd /root/python
git pull origin master
nohup python3 index.py > /var/log/nohup.log &
