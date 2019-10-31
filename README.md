# LCD
This repository contains all of the code for interfacing with a 16x2 Character I2C LCD Display. This accompanies my YouTube tutorial here: https://www.youtube.com/watch?v=fR5XhHYzUK0 

To install, type commands:
```
sudo git clone https://github.com/akcryptoguy/lcd
cd lcd
sudo sh install.sh
```


To add a script to run as a service, enter cron and add the following:
@reboot sudo python (TYPE IN THE LOCATION OF YOUR CRYPTOTICKER.PY FILE)
@reboot python /home/pi/lcd/ticker.py

You can buy one of these great little I2C LCD Displays for just £4.99 on ryanteck.uk: https://ryanteck.uk/displays/11-16x2-character-i2c-lcd-display.html

## Pin these 4 wires
```
GRND on display to pin 6 on Pi
VCC on display to pin 2 on Pi
SDA on display to pin 3 on Pi
SCL on display to pin 5 on Pi
```


Editing rc.local

On your Pi, edit the file /etc/rc.local using the editor of your choice. You must edit it with root permissions:

sudo nano /etc/rc.local

Add commands to execute the python program, preferably using absolute referencing of the file location (complete file path are preferred). Be sure to leave the line exit 0 at the end, then save the file and exit. In nano, to exit, type Ctrl-x, and then Y.

Edit RC Local File Configure Run a Program On Your Raspberry Pi At Startup

If your program runs continuously (runs an infinite loop) or is likely not to exit, you must be sure to fork the process by adding an ampersand (“&”) to the end of the command, like:

sudo python /home/pi/sample.py &

The Pi will run this program at bootup, and before other services are started.  If you don’t include the ampersand and if your program runs continuously, the Pi will not complete its boot process. The ampersand allows the command to run in a separate process and continue booting with the main process running.
