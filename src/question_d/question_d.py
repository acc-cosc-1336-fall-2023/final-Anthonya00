#write functions here, don't add input('') statements here!

class stock():
    __symbol = None
    __company_name = None 
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name
    
def write_file(file):
    enter_file = open(file,'w')
    symbols = ['APPL', 'CAT', 'EK','GOOG','MSFT']
    companies = ['Apple Inc', 'Caterpillar', 'Eastman Kodak', 'Google', 'Microsoft' ]
    for i in range(len(symbols)):
        enter_file.write(symbols[i] + " " + companies[i] + '\n')
    enter_file.close()

def get_stock_list(file_name):
    dictionary = {}
    in_file = open(file_name, 'r')
    for i in in_file:
        symbol, company_name = i.strip().split(' ', 1)
        stocks = stock(symbol, company_name)
        dictionary[symbol] = stocks
    return dictionary