#!/bin/bash
echo -e " $(date +%m.%d.%Y_%H:%M:%S) : About to reboot " | tee -a /home/pi/cronlog

# clear out all but the last 28 log entries
# count number of lines in the file, save to variable
LINES=$(wc -l /home/pi/cronlog | awk '{ print $1 }')
# determine how many lines to remove
EXTRA=$(( $LINES - 28 ))
# delete range of lines 1 through difference above
if (( $EXTRA >= 1 ))
then sed -i "1,${EXTRA}d" /home/pi/cronlog
fi

sudo /sbin/shutdown -r now
