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

You can buy one of these great little I2C LCD Displays for just £4.99 on ryanteck.uk: https://ryanteck.uk/displays/11-16x2-character-i2c-lcd-display.html

## Pin these 4 wires
```
GRND on display to pin 6 on Pi
VCC on display to pin 2 on Pi
SDA on display to pin 3 on Pi
SCL on display to pin 5 on Pi
```
