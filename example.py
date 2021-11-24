from QiubyZEtherChain.EtherBlock import BinanceSmartChain, PolygonScan, Ethereum
print("Binance SmartChain Explorer")
sc = "0xcE8b739b3f1624D359e5F8E9ea72A826f1d48178"
bsc = BinanceSmartChain(sc)
print(bsc.getToken())

print("Polygon Exlorer")
polygon_address = "0xfCbAC176e8b54E6A770F7Ca16AcB51954f9A4D80"
polygon_explorer = PolygonScan(polygon_address)
print(polygon_explorer.getToken())

print('Ethereum explorer')
ether_address = "0xbccf0cab5af77d4af3b30539a7c09d0307d66e57"
ether_explorer = Ethereum(ether_address)
print(ether_explorer.getToken())

