import requests
import bs4

r = requests.get("https://www.tradingview.com/symbols/NASDAQ-AAPL/technicals/")
bs = bs4.BeautifulSoup(r.text)
print(bs.get_text())
