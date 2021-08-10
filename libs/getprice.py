from requests import Session
from decimal import Context
from bs4 import BeautifulSoup as Parser

class PancakeSwap(Session):
	def __init__(self, version="v2"):
		super(PancakeSwap, self).__init__()
		self.ctx = Context()
		self.url = f"https://api.pancakeswap.info/api/{version}/"
		self.result = None
		
	def setToken(self, ContractAdress):
		result_data = self.get(f"{self.url}tokens/{ContractAdress}").json().get("data")
		self.result = result_data if result_data != None else {}
		
	def getvalue(self, x):
		return self.result.get(x, f"Tidak Ada {x}")
		
	def getPrice(self):
		return self.getvalue("price")
		
	def getprice_BNB(self):
		return self.getvalue('price_BNB')
		
	def getsymbol(self):
		return self.getvalue('symbol')
		
	def getname(self):
		return self.getvalue("name")
		
	def convert(self, price):
		self.ctx.prec = len(price)
		return self.ctx.create_decimal(price)
        
class Blockchain(Session):
	def __init__(self, url):
		super(Blockchain, self).__init__()
		self.block_chain = url
		
	def _get_parser(self):
		parser = Parser(self.get(self.block_chain).text, "html.parser")
		return parser