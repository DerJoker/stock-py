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
        print time.asctime()
        for item in stinfo.parseResults():
            print item

# timer = threading.Timer(30, notification)
# timer.start()

while True:
    event = threading.Event()
    # check every 60s
    event.wait(timeout=6)
    notification()