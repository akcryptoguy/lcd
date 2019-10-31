# Created 06/09/2018 by reddit user anonananananabatman
# Made available under GNU GENERAL PRIVATE LICENSE
# ver 1.0

import time
import json
import requests
import lcddriver

mylcd = lcddriver.lcd()
mylcd.lcd_clear()

# Display loading string
mylcd.lcd_display_string("Working...")

# Create font for arrows
fontdata1 = [
    [0b00000,
	0b00100,
	0b00100,
	0b01110,
	0b01110,
	0b11111,
	0b11111,
	0b00000],

    [0b00000,
	0b11111,
	0b11111,
	0b01110,
	0b01110,
	0b00100,
	0b00100,
	0b00000],

    [0b00000,
	0b00100,
	0b01110,
	0b11111,
	0b00000,
	0b11111,
	0b01110,
	0b00100],
    ]

# import font data
mylcd.lcd_load_custom_chars(fontdata1)

# set variables for last price of currency
lastPrice = 0
lastPrice1 = 0
lastPrice2 = 0
lastPrice3 = 0

# Preload btc price before beginning while loop
def btcPrice():
    try:
        b = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
        priceFloat = float(json.loads(b.text)['USD'])
        return priceFloat
    except requests.ConnectionError:
        print ("Error querying Crytocompare API")

# Determines direction of the arrow
def arrow_dir():

    currentPrice = btcPrice()
    
    if lastPrice == currentPrice:
        return 2
    elif lastPrice > currentPrice:
       return 1
    elif lastPrice < currentPrice:
        return 0

# Waits 5 seconds
time.sleep(5)

# Display time and date
mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2, 0)

while True:

# Writes BTC price to LCD 
    mylcd.lcd_write(0x80)
    mylcd.lcd_display_string("                ")
    time.sleep(0.4)
    mylcd.lcd_display_string("$" + str(btcPrice()) + "/BTC   ", 1)
    mylcd.lcd_write_char(arrow_dir())

    print("$" + str(btcPrice()) + "/BTC " + str(arrow_dir()))
    lastPrice = btcPrice()

# Pulls ETH price
    def ethPrice():
        try:
            e = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
            priceFloat1 = float(json.loads(e.text)['USD'])
            return priceFloat1
        except requests.ConnectionError:
            print ("Error querying CoinBase API")

    def arrow_dir1():

        currentPrice1 = ethPrice()
    
        if lastPrice1 == currentPrice1:
            return 2
        elif lastPrice1 > currentPrice1:
            return 1
        elif lastPrice1 < currentPrice1:
            return 0

    time.sleep(5)

    mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2, 0)

# Writes ETH price to the LCD
    mylcd.lcd_write(0x80)
    mylcd.lcd_display_string("                ")
    time.sleep(0.4)
    mylcd.lcd_display_string("$" + str(ethPrice()) + "/ETH    ", 1)
    mylcd.lcd_write_char(arrow_dir1())

    print("$" + str(ethPrice()) + "/ETH " + str(arrow_dir1()))
    lastPrice1 = ethPrice()

# Pulls LTC price
    def ltcPrice():
        try:
            l = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD')
            priceFloat2 = float(json.loads(l.text)['USD'])
            return priceFloat2
        except requests.ConnectionError:
            print ("Error querying Crytocompare API")

    def arrow_dir2():

        currentPrice2 = ltcPrice()
    
        if lastPrice2 == currentPrice2:
            return 2
        elif lastPrice2 > currentPrice2:
            return 1
        elif lastPrice2 < currentPrice2:
            return 0
    time.sleep(5)

    mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2, 0)

# Writes LTC price to the display
    mylcd.lcd_write(0x80)
    mylcd.lcd_display_string("                ")
    time.sleep(0.4)
    mylcd.lcd_display_string("$" + str(ltcPrice()) + "/LTC    ", 1)
    mylcd.lcd_write_char(arrow_dir2())

    print("$" + str(ltcPrice()) + "/LTC " + str(arrow_dir2()))
    lastPrice2 = ltcPrice()

# Determines XRP price
    def xrpPrice():
        try:
            x = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD')
            priceFloat3 = float(json.loads(x.text)['USD'])
            return priceFloat3
        except requests.ConnectionError:
            print ("Error querying Crytocompare API")

    def arrow_dir3():

        currentPrice3 = xrpPrice()
    
        if lastPrice3 == currentPrice3:
            return 2
        elif lastPrice3 > currentPrice3:
            return 1
        elif lastPrice3 < currentPrice3:
            return 0
    time.sleep(5)

    mylcd.lcd_display_string(("%s" %time.strftime("%H:%M   ")) + ("%s" %time.strftime("%m/%d/%y")), 2, 0)

# Writes XRP price to LCD
    mylcd.lcd_write(0x80)
    mylcd.lcd_display_string("                ")
    time.sleep(0.4)
    mylcd.lcd_display_string("$" + str(xrpPrice()) + "/XRP    ", 1)
    mylcd.lcd_write_char(arrow_dir3())

    print("$" + str(xrpPrice()) + "/XRP " + str(arrow_dir3()))
    lastPrice3 = xrpPrice()

# Determines BTC price
    def btcPrice():
        try:
            r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
            priceFloat = float(json.loads(r.text)['USD'])
            return priceFloat
        except requests.ConnectionError:
            print ("Error querying CoinBase API")

    def arrow_dir():

        currentPrice = btcPrice()
    
        if lastPrice == currentPrice:
            return 2
        elif lastPrice > currentPrice:
            return 1
        elif lastPrice < currentPrice:
            return 0
        
    time.sleep(5)
