#!/bin/bash

echo -e "  --> Add cron to reboot every 4 hours"
crontab -l
(crontab -l ; echo "0 */4 * * * /sbin/shutdown -r now") | crontab -

exit