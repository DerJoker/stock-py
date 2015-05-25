import threading, time

from stock import Stock
import config

debug = True
debug = False

# stocks to monitor
stocks = []
with open(config._path_stocks_txt) as f_stocks_txt:
    for line in f_stocks_txt.readlines():
        symbol, ownership = eval(line.split('#')[0])
        stocks.append(Stock(symbol, ownership))

def notification():

    for stock in stocks:
        
        c1 = stock.calculate()
        
        delta = 20
        eventdelta = threading.Event()
        # check every 20s
        eventdelta.wait(timeout=delta)
        
        c2 = stock.calculate()
        
        allowance = 0.01
        # c1 > c2: decrease
        if c1 - c2 > allowance and stock.ownership:
            print time.ctime(), 'selling point', stock.getCompanyName()
        # c1 < c2: increase
        if c2 - c1 > allowance and not stock.ownership:
            print time.ctime(), 'buying point', stock.getCompanyName()

# timer = threading.Timer(30, notification)
# timer.start()

while True:
    notification()