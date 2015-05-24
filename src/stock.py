from sina import StockInfo

CODEC = 'gb2312'

debug = True
debug = False

'''
What's of interest to me is:
    - turning point
    - big amount of buys and sells
'''

class Stock:
    
    def __init__(self, symbol, ownership):
        self.symbol = symbol
        self.ownership = ownership    # True: to sell, or False: to buy
        with open(self.symbol, 'w') as f:
            f.close()
    
    def getCompanyName(self):
        return StockInfo(self.symbol).getCompanyName()
    
    def calculate(self):
        stinfo = StockInfo(self.symbol)
        with open(self.symbol, 'a') as f:
            if (debug): print stinfo.buffer
            f.write(stinfo.buffer.encode(CODEC))
            f.close()
        return stinfo.getPrice() / stinfo.getPriceTodayOpen() - 1


'''
UnitTest
'''

if __name__ == '__main__':
    
    stocks = [('sh600030', True), ('sh600547', False), ('sh600151', False), ('sz000593', True), ('sz002029', False)]
    
    for (symbol, ownership) in stocks:
        stock = Stock(symbol, ownership)
        print stock.getCompanyName(), stock.calculate()