from requests import Session
from decimal import Context
from bs4 import BeautifulSoup as Parser

class PancakeSwap(Session):
	def __init__(self, version="v2"):
		super(PancakeSwap, self).__init__()
		self.__ctx = Context()
		self.__url = f"https://api.pancakeswap.info/api/{version}/"
		self.__result = None
		
	def setToken(self, ContractAdress):
		result_data = self.get(f"{self.__url}tokens/{ContractAdress}").json().get("data")
		self.__result = result_data if result_data != None else {}
		
	def getvalue(self, x):
		return self.__result.get(x, f"Tidak Ada {x}")
		
	def getPrice(self):
		return self.getvalue("price")
		
	def getprice_BNB(self):
		return self.getvalue('price_BNB')
		
	def getsymbol(self):
		return self.getvalue('symbol')
		
	def getname(self):
		return self.getvalue("name")
		
	def convert(self, price):
		self.__ctx.prec = len(price)
		return self.__ctx.create_decimal(price)
        
class Blockchain(Session):
	def __init__(self, url):
		super(Blockchain, self).__init__()
		self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
		self.__block_chain = url
		
	def _get_parser(self):
		parser = Parser(self.get(self.__block_chain).text, "html.parser")
		return parser
