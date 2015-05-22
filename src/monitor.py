import threading, time

from sina import StockInfo

debug = True
debug = False

# stocks to monitor
'''
Gong Shang Yin Hang: sh601398
Zhong Yuan Hang Yun: sh600428

For Test
Qi Pi Lang: sz002029
'''
stocks = ['sh601398','sh600428','sz002029']

def notification():

    for s in stocks:
        stinfo = StockInfo(s)
        price_yesterday_close = stinfo.getPriceYesterdayClose()
        price = stinfo.getPrice()
        rate = price / price_yesterday_close - 1
        print time.asctime()
        print rate

# timer = threading.Timer(30, notification)
# timer.start()

while True:
    notification()
    event = threading.Event()
    # check every 60s
    event.wait(timeout=6)