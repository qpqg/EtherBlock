from QiubyZEtherChain.libs.getprice import PancakeSwap
from QiubyZEtherChain.EtherBlock import BinanceSmartChain

print("Binance SmartChain Explorer")
bsc_market = PancakeSwap()
sc = "0xcE8b739b3f1624D359e5F8E9ea72A826f1d48178"

bsc = BinanceSmartChain(sc)

for myjson in bsc.getToken():
  contract_address_token = myjson.get('contract')
  token_name = myjson.get('nama')
  symb = myjson.get('symbol')
  value_token = myjson.get("jumlah_token")
  bsc_market.setToken(contract_address_token)
  price_pancakce = bsc_market.getprice_BNB()
  switch_case = {"Tidak Ada price_BNB":"No Liquidity", "0":"Required Approve"}.get(price_pancakce) or price_pancakce
  print(f"Name: {token_name}\nValues: {value_token} {symb}\nPancakeSwap Price: {switch_case}\nContract Address: {contract_address_token}\r\n")
