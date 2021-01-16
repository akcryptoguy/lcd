#!/bin/sh
# kill and restart the ticker script
sudo pkill python
sleep .25
sudo python /home/pi/lcd/btc_ticker.py
