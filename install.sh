#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "Please re-run as sudo."
	exit 1
fi

echo "Automated Installer Program For I2C LCD Screens"
echo "Installer by Ryanteck LTD. Cloned and tweaked by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube tutorial"
echo "Updating APT & Installing python-smbus, if password is asked by sudo please enter it"
apt-get update
apt-get install python-smbus -y
apt-get install python-requests -y
echo "Should now be installed, now checking revision"
revision=`python -c "import RPi.GPIO as GPIO; print GPIO.RPI_REVISION"`

if [ $revision = "1" ]
then
echo "I2C Pins detected as 0"
cp installConfigs/i2c_lib_0.py ./i2c_lib.py
else
echo "I2C Pins detected as 1"
cp installConfigs/i2c_lib_1.py ./i2c_lib.py
fi
echo "I2C Library setup for this revision of Raspberry Pi, if you change revision a modification will be required to i2c_lib.py"
echo "Now overwriting modules & blacklist. This will enable i2c Pins"
cp installConfigs/modules /etc/
cp installConfigs/raspi-blacklist.conf /etc/modprobe.d/
printf "dtparam=i2c_arm=1\n" >> /boot/config.txt

sudo chmod +x /home/pi/lcd/*.py
sudo chmod +x /home/pi/lcd/*.sh

cat <<EOT > /etc/rc.local
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi
sudo python /home/pi/lcd/btc_ticker.py &
exit 0

EOT

echo -e "  --> Add cron to reboot every 4 hours"
(crontab -l ; echo "*/20 * * * * sudo bash /home/pi/lcd/checknet.sh") | crontab -
(crontab -l ; echo "5 */1 * * * sudo bash /home/pi/lcd/btc-cron.sh") | crontab -
(crontab -l ; echo "2 */8 * * * sudo bash /home/pi/lcd/reboot.sh") | crontab -


echo "Should be now all finished. Will reboot in 10 seconds."
sleep 10
sudo reboot
