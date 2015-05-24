import threading, time

from stock import Stock
import config

debug = True
debug = False

# stocks to monitor
stocks = []
with open(config._path_stocks_txt) as f_stocks_txt:
    for line in f_stocks_txt.readlines():
        stocks.append(eval(line.split('#')[0]))
print stocks

def notification():

    for (symbol, ownership) in stocks:
        stock = Stock(symbol, ownership)
        print stock.calculate()
        print 'system time:', time.time()

# timer = threading.Timer(30, notification)
# timer.start()

while True:
    notification()
    event = threading.Event()
    # check every 60s
    event.wait(timeout=6)