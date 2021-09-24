from QiubyZEtherChain.libs import RequestOveride
from decimal import Context

class DecimalsConverter(Context):
	def __init__(self, price):
		super(DecimalsConverter, self).__init__()
		self.prec = len(price)

	def convert(self, price):
		return self.create_decimal(price)

class PancakeSwap(RequestOveride.Blockchain):
	def __init__(self, version="v2"):
		super(PancakeSwap, self).__init__()
		self._block_chain = f"https://api.pancakeswap.info/api/{version}/"
		self.__result = None
		self.__contract = None
		
	def setToken(self, ContractAdress):
		self.__contract = ContractAdress
		result_data = self.get(f"{self._block_chain}tokens/{ContractAdress}").json().get("data")
		self.__result = result_data if result_data != None else {}

	def getvalue(self, x):
		return self.__result.get(x, f"Tidak Ada {x}")
		
	def getPrice(self):
		return self.getvalue("price")
		
	def getprice_BNB(self):
		real_price = self.getvalue('price_BNB')
		return real_price

	def getsymbol(self):
		return self.getvalue('symbol')
		
	def getname(self):
		return self.getvalue("name")
