echo pulling from master...
cd /home/pi/PiPager
git reset --hard
git pull origin master
sudo python3 setup.py
cd ../
