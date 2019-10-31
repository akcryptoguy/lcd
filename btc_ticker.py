#script by: u/SakamotoDesu
#edited by: u/AKcryptoGUY
 
import lcddriver
import requests, time
 
display = lcddriver.lcd()
 
try:
    while True:
        price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        dom = requests.get("https://api.coinpaprika.com/v1/global").json()
        display.lcd_clear()
        display.lcd_display_string("BTC: $ " + str(price['bitcoin']['usd']), 1)
        display.lcd_display_string("MARKET: " + str(dom['bitcoin_dominance_percentage']) + "%", 2)
        time.sleep(10)
 
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
