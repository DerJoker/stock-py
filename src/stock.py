from sina import StockInfo

'''
What's of interest to me is:
    - turning point
    - big amount of buys and sells
'''

class Stock:
    
    def __init__(self, symbol, ownership):
        self.symbol = symbol
        self.ownership = ownership    # True: to sell, or False: to buy
    
    def getCompanyName(self):
        return StockInfo(self.symbol).getCompanyName()
    
    def calculate(self):
        stinfo = StockInfo(self.symbol)
        return stinfo.getPrice() / stinfo.getPriceTodayOpen() - 1


'''
UnitTest
'''

if __name__ == '__main__':
    
    stocks = [('sh600030', True), ('sh600547', False), ('sh600151', False), ('sz000593', True), ('sz002029', False)]
    
    for (symbol, ownership) in stocks:
        stock = Stock(symbol, ownership)
        print stock.getCompanyName(), stock.calculate()