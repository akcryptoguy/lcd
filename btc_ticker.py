# script by: u/SakamotoDesu
# edited by: u/AKcryptoGUY
import lcddriver
import requests, time
display = lcddriver.lcd()
try:
    print("Writing Prices to display")
    while True:
        price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        priceeth = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd").json()
        dom = requests.get("https://api.coinpaprika.com/v1/global").json()
        display.lcd_clear()
        display.lcd_display_string("  BTC: $ " + str(price['bitcoin']['usd']), 1)
        display.lcd_display_string("  ETH: $  " + str(priceeth['ethereum']['usd']), 2)
        time.sleep(20)
        display.lcd_clear()
        display.lcd_display_string("Price Refresh in ", 1)
        display.lcd_display_string("  40 seconds ", 2)
        time.sleep(2)
        display.lcd_clear()
        display.lcd_display_string("  BTC: $ " + str(price['bitcoin']['usd']), 1)
        display.lcd_display_string("  ETH: $  " + str(priceeth['ethereum']['usd']), 2)
        time.sleep(20)
        display.lcd_clear()
        display.lcd_display_string("Price Refresh in ", 1)
        display.lcd_display_string("  20 seconds ", 2)
        time.sleep(2)
        display.lcd_clear()
        display.lcd_display_string("  BTC: $ " + str(price['bitcoin']['usd']), 1)
        display.lcd_display_string("  ETH: $  " + str(priceeth['ethereum']['usd']), 2)
        time.sleep(20)
        display.lcd_clear()
        display.lcd_display_string("  Refreshing", 1)
        display.lcd_display_string("   Price Now", 2)
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()