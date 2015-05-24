import urllib2, time

CODEC = 'gb2312'

debug = True
debug = False

class StockInfo:
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.buffer = self.read().decode(CODEC)
        self.infolist = self.buffer.split(',')
        if (debug): print 'StockInfo: __init__', self.infolist
    
    def read(self):
        '''
        -> str
        
        Return empty string if TimeOut
        '''
        url = 'http://hq.sinajs.cn/list=' + self.symbol
        res = ''
        
        while (res == ''):
            try:
                res = urllib2.urlopen(url, timeout=10).read()
            except Exception,e:
                if (debug): print e
                res = ''
        
        return res
    
    def getCompanyName(self):
        '''
        -> str
        '''
        return self.infolist[0].split('"')[-1]
    
    def getPriceYesterdayClose(self):
        '''
        -> float
        
        price_yesterday_close can be 0 (because of suspending)
        '''
        return float(self.infolist[1])
    
    def getPriceTodayOpen(self):
        '''
        -> float
        '''
        return float(self.infolist[2])
    
    def getPrice(self):
        '''
        -> float
        '''
        return float(self.infolist[3])
    
    def getTime(self):
        '''
        -> time
        '''
#         return self.infolist[30] + ' ' + self.infolist[31]
        return time.mktime(time.strptime(self.infolist[30] + ' ' + self.infolist[31], '%Y-%m-%d %H:%M:%S'))
    
    def parseResults(self):
        company_name = self.infolist[0].split('"')[-1]
        price_yesterday_close = self.infolist[1]
        price_today_open = self.infolist[2]
        price = self.infolist[3]
        return (company_name, self.symbol, price)


'''
UnitTest
'''

if __name__ == '__main__':
    
    stocks = ['sh600030', 'sh600547', 'sh600151', 'sz000593', 'sz002029']
    
    for s in stocks:
        stinfo = StockInfo(s)
        print stinfo.getTime()
        for item in stinfo.parseResults():
            print item