#!/bin/bash
ping -c 4 google.com
let a=$?
if [ "$a" = "0" ]; then
  echo "We have connection."
else
  echo "We have lost connection.."

# clear out all but the last 28 log entries
# count number of lines in the file, save to variable
LINES=$(wc -l /home/pi/cronlog | awk '{ print $1 }')
# determine how many lines to remove
EXTRA=$(( $LINES - 28 ))
# delete range of lines 1 through difference above

if (( $EXTRA >= 1 ))
then sed -i "1,${EXTRA}d" /home/pi/cronlog
fi

echo -e " $(date +%m.%d.%Y_%H:%M:%S) : Network lost: about to reboot " | tee -a /home/pi/cronlog
sudo /sbin/shutdown -r now

fi
