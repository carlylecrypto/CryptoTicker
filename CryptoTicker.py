
from datetime import datetime
from time import sleep
import I2C_LCD_driver

display = I2C_LCD_driver.lcd()

display.lcd_display_string("CryptoTicker",1)

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


#Only bits that you need to change -----------------
#Any coin listed on CoinGecko is valid
coinList = ['bitcoin', 'ethereum', 'cardano'] #Add the cryptos you want in here (lowercase and check your spelling!)
currency = 'gbp' #The currency code (lowercase) e.g. usd for US Dollars, gbp for British Pounds
sleepTime = 4 #The number of seconds between each crypto
#Don't touch anything else! ------------------------


coinDict = cg.get_price(ids=coinList, vs_currencies=currency, include_24hr_change='true', include_last_updated_at='true')

while True:
        coinDict = cg.get_price(ids=coinList, vs_currencies=currency, include_24hr_change='true', include_last_updated_at='true')
        for coin in coinList:
                display.lcd_clear()
                coinName = coin.title()
                coinPrice = coinDict[coin][currency]
                coinChange = float(coinDict[coin][currency+'_24h_change'])
                if coinChange >= 0:
                        coinChange = "UP"
                else:
                        coinChange = "DOWN"
                coinTime = coinDict[coin]['last_updated_at']
                coinTime = datetime.fromtimestamp(coinTime).time()
                #print(coinName, coinPrice, coinChange, coinTime)
                display.lcd_display_string(coinName,1,0)
                display.lcd_display_string(str(coinPrice),1,9)
                display.lcd_display_string(str(coinTime),2,0)
                display.lcd_display_string(coinChange,2,9)
                sleep(sleepTime)
