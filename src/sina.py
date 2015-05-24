import urllib2

CODEC = 'gb2312'

debug = True
debug = False

class StockInfo:
    
    def __init__(self, symbol):
        self.symbol = symbol
    
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
        if (debug): print self.read().decode(CODEC)
        return self.read().decode(CODEC).split(',')[0].split('"')[-1]
    
    def getPriceYesterdayClose(self):
        '''
        -> float
        
        price_yesterday_close can be 0 (because of suspending)
        '''
        if (debug): print self.read().decode(CODEC)
        return float(self.read().decode(CODEC).split(',')[1])
    
    def getPriceTodayOpen(self):
        '''
        -> float
        '''
        if (debug): print self.read().decode(CODEC)
        return float(self.read().decode(CODEC).split(',')[2])
    
    def getPrice(self):
        '''
        -> float
        '''
        if (debug): print self.read().decode(CODEC)
        return float(self.read().decode(CODEC).split(',')[3])
    
    def parseResults(self):
        if (debug): print self.read().decode(CODEC)
        res = self.read().decode(CODEC).split(',')
        
        company_name = res[0].split('"')[-1]
        price_yesterday_close = res[1]
        price_today_open = res[2]
        price = res[3]
        return (company_name, self.symbol, price)


'''
UnitTest
'''

if __name__ == '__main__':
    
    stocks = ['sh600030', 'sh600547', 'sh600151', 'sz000593', 'sz002029']
    
    for s in stocks:
        stinfo = StockInfo(s)
        for item in stinfo.parseResults():
            print item