#!/bin/bash

echo running PiPager
git pull origin master
sudo /usr/bin/python3 /home/pi/PiPager/main.py > /home/pi/PiPager/pager.log 2>&1 &
