# from libs.getprice import SmartChain
from blockchain.EtherBlock import BinanceSmartChain, PolygonScan, Ethereum
print("Binance SmartChain")
sc = "0xcE8b739b3f1624D359e5F8E9ea72A826f1d48178"
bsc = BinanceSmartChain(sc)
print(bsc.getToken())

print("Polygon Scan")
matic = "0xfCbAC176e8b54E6A770F7Ca16AcB51954f9A4D80"
mitic = PolygonScan(matic)
print(mitic.getToken())

print("Ether Scan")
ether = "0xfCbAC176e8b54E6A770F7Ca16AcB51954f9A4D80"
ether = Ethereum(ether)
print(ether.getToken())