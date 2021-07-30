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
		
	def get_parser(self):
		parser = Parser(self.get(self.block_chain).text, "html.parser")
		return parser

class SmartChain(Blockchain):
	def __init__(self, Address_Wallet):
		super(SmartChain, self).__init__(f"http://bscscan.com/address/{Address_Wallet}")
		self.tokenize = {"wallet":Address_Wallet, "token":[]}
		self.check_price = PancakeSwap()
		self.getScan()
		
	def gettotal(self):
		return (len(self.tokenize.get("token")))
		
	def getJson(self):
		return self.tokenize
		
	def getWallet(self):
		return self.tokenize.get("wallet")
		
	def getToken(self):
		return self.tokenize.get("token")
	
	def getScan(self):
		listtoken = self.get_parser().find("ul", {"class":"list list-unstyled mb-0"})
		token_list = listtoken.find_all_next("a", {"class": "link-hover d-flex justify-content-between align-items-center"})
		for i in range(len(token_list)):
			price = token_list[i].find("span",{"class":"list-usd-value d-block"})
			if(price):
				price = price.text if price.text != "\xa0" else "Tidak ada"
			else:
				price = "Tidak Ada"
			contract_token = token_list[i]["href"].split("?")[0].replace("/token/", "")
			token_info = token_list[i].find("span", {"class":"list-amount link-hover__item hash-tag hash-tag--md text-truncate"})
			if(token_info):
				token_value, symbl = token_info.text.split(" ")	
			Token_name = token_list[i].find("span", {"class":"list-name hash-tag text-truncate"}).text
			self.check_price.setToken(contract_token)		
			format_save = {
				"nama":f"{Token_name}",
				"symbol": f"{symbl}",
				"contract": f"{contract_token}",
				"jumlah_token": f"{token_value}",
				"usd":f"{price}",
				"price_bnb":f"{self.check_price.getprice_BNB()}"}
			self.tokenize.get("token").append(format_save)				          		  
