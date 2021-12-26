#!/bin/bash

echo running PiPager
sh update.sh
sudo /usr/bin/python3 /home/pi/PiPager/main.py > /home/pi/PiPager/pager.log 2>&1 &
