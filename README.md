# BlockChain API

Api yang sengaja dibuat untuk mengambil Info Token dari BlockChain BinanceChain dan PolyGon, yang sangat simple
untuk digunakan. Price diambel berdasarkan Price USDT Yang tersedia dalam Blockchain itu sendiri "Jika ada".
# Example

```python
from blockchain.EtherBlock import BinanceSmartChain, PolygonScan, Ethereum
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

```
output

```
Binance SmartChain
[{'nama': 'DeFi For You... (DFY)', 'symbol': 'DFY', 'contract': '0xd98560689c6e748dc37bc410b4d3096b1aa3d8c2', 'jumlah_token': '2.42', 'usd': '$0.24'}, {'nama': 'Spore (SPORE)', 'symbol': 'SPORE', 'contract': '0x33a3d962955a3862c8093d1273344719f03ca17c', 'jumlah_token': '2,920,837,050.80414', 'usd': '$0.29'}, {'nama': 'Agrinoble (AGN)', 'symbol': 'AGN', 'contract': '0x2317f8c321954070b57019bfbd9a1fae1f3c04d9', 'jumlah_token': '10,900', 'usd': 'Tidak ada'}, {'nama': 'ALPACAFIN.CO... (ALPACA)', 'symbol': 'ALPACA', 'contract': '0x373233A38ae21cF0C4f9DE11570E7D5Aa6824A1E', 'jumlah_token': '28,102,000', 'usd': 'Tidak ada'}, {'nama': 'Automata (ATA)', 'symbol': 'ATA', 'contract': '0x7159b835cbeb8d01136d6cc321018b60ccec4b30', 'jumlah_token': '50', 'usd': 'Tidak ada'}, {'nama': 'Baby Doge Co... (BabyDo...)', 'symbol': 'BabyDoge', 'contract': '0xc748673057861a797275CD8A068AbB95A902e8de', 'jumlah_token': '252,291,809.868527', 'usd': '$0.50'}, {'nama': 'Beer Money (BEER)', 'symbol': 'BEER', 'contract': '0x05a00764d371774831a48b3f57ef9073710c5fd8', 'jumlah_token': '3', 'usd': 'Tidak ada'}, {'nama': 'BITCHIP (CHIP)', 'symbol': 'CHIP', 'contract': '0x7ea2b25c1a558c6f9b4649358183152b0ea4c03f', 'jumlah_token': '2,850,000,000', 'usd': 'Tidak ada'}, {'nama': 'BNBL TOKEN (BNBL)', 'symbol': 'BNBL', 'contract': '0xae5fe46135481cdc5815e191b3a3c9f31bdfe442', 'jumlah_token': '50', 'usd': 'Tidak ada'}, {'nama': 'ChesterCoin (CTRFI)', 'symbol': 'CTRFI', 'contract': '0xb74ed4112c23b7c8ef1439fa55d304d537c5599b', 'jumlah_token': '14,766,732,003.9107', 'usd': 'Tidak ada'}, {'nama': 'Corgi doge (CORGI)', 'symbol': 'CORGI', 'contract': '0x802c68730212295149f2bea78c25e2cf5a05b8a0', 'jumlah_token': '105,000', 'usd': '$0.08'}, {'nama': 'Crox Token (CROX)', 'symbol': 'CROX', 'contract': '0x2c094f5a7d1146bb93850f629501eb749f6ed491', 'jumlah_token': '2.25172299', 'usd': '$0.28'}, {'nama': 'Ether2 (ETHER2)', 'symbol': 'ETHER2', 'contract': '0x3fe5682df4f362a272d30da5e41d0003d5605045', 'jumlah_token': '250,000,000', 'usd': 'Tidak ada'}, {'nama': 'Fire Protoco... (FPF)', 'symbol': 'FPF', 'contract': '0x75b25dcfa0a3da2fe07c4840d2230c0412cbedac', 'jumlah_token': '32', 'usd': 'Tidak ada'}, {'nama': 'FishSwap (FISH)', 'symbol': 'FISH', 'contract': '0xd9a0dc07d25ed65da8ed4321c42f7f35de81bf2d', 'jumlah_token': '11', 'usd': 'Tidak ada'}, {'nama': 'GoFlux.io (FLUX)', 'symbol': 'FLUX', 'contract': '0xb16600c510b0f323dee2cb212924d90e58864421', 'jumlah_token': '950,000', 'usd': 'Tidak ada'}, {'nama': 'Gold Bee (GBE)', 'symbol': 'GBE', 'contract': '0xf9a5e6533e4cb0791ecbb79f710ee8ee980eb853', 'jumlah_token': '169.32302137', 'usd': 'Tidak ada'}, {'nama': 'HelloSwap To... (HELLO)', 'symbol': 'HELLO', 'contract': '0x4fa55d435ef98ad77c1efa25ae764ccb858f7046', 'jumlah_token': '5,200', 'usd': 'Tidak ada'}, {'nama': 'Investelly (INVEST...)', 'symbol': 'INVESTEL', 'contract': '0xb3ceb24a344fc90289f0255169c3ef65e643f137', 'jumlah_token': '10', 'usd': 'Tidak ada'}, {'nama': 'Koda Robot D... (KODA)', 'symbol': 'KODA', 'contract': '0x319f6c64247972f0377a5ca934c61c95036df231', 'jumlah_token': '1,532,286.80001067', 'usd': 'Tidak ada'}, {'nama': 'Lindalit BSC (LINDA)', 'symbol': 'LINDA', 'contract': '0x1002d9f872e87090b67ea0242e1a3af2164a3732', 'jumlah_token': '0.00087591', 'usd': 'Tidak ada'}, {'nama': 'Lock Chain F... (LOCKCH...)', 'symbol': 'LOCKCHAIN', 'contract': '0xac4c2903fb2f073e94de57c79d8bec5155662122', 'jumlah_token': '2,750,000', 'usd': 'Tidak ada'}, {'nama': 'Medical Veda (MVEDA)', 'symbol': 'MVEDA', 'contract': '0xe73bb2b15f0a5f45729a9f6c4a9a51b380bf0dff', 'jumlah_token': '3,500,000', 'usd': 'Tidak ada'}, {'nama': 'Minereum BSC (MNEB)', 'symbol': 'MNEB', 'contract': '0xd22202d23fe7de9e3dbe11a2a88f42f4cb9507cf', 'jumlah_token': '150,000', 'usd': 'Tidak ada'}, {'nama': 'Moon Chain (MCF)', 'symbol': 'MCF', 'contract': '0x6fc015dc3283369125cc31907eef990b8f67a7a1', 'jumlah_token': '1,000,000', 'usd': 'Tidak ada'}, {'nama': 'Moon Stake (MSEF)', 'symbol': 'MSEF', 'contract': '0x63c500b0bfeb042ff70ea2450aeba72713d10668', 'jumlah_token': '20,000', 'usd': 'Tidak ada'}, {'nama': 'Nyan Cat Tok... (NCAT)', 'symbol': 'NCAT', 'contract': '0x0cF011A946f23a03CeFF92A4632d5f9288c6C70D', 'jumlah_token': '42,529,631.3077643', 'usd': '$0.11'}, {'nama': 'Poodledog To... (POODLE)', 'symbol': 'POODLE', 'contract': '0x4487a8a40caa9fa0e70b9041c368b6e0d4089314', 'jumlah_token': '25', 'usd': 'Tidak ada'}, {'nama': 'SAFE MERCURY (SMRCY)', 'symbol': 'SMRCY', 'contract': '0xe1dBf7F4b4852d97095344CB2d97e01Cbc80b581', 'jumlah_token': '1,188,841.64349208', 'usd': 'Tidak ada'}, {'nama': 'Safe Nebula (SNB)', 'symbol': 'SNB', 'contract': '0x5e7fc3844463745fca858f85d6b90d9a03fcbe93', 'jumlah_token': '250,000,000', 'usd': 'Tidak ada'}, {'nama': 'SafeGas (SAFEGA...)', 'symbol': 'SAFEGAS', 'contract': '0xdbd083b36e07859f20ad0010366c748faf04ca0b', 'jumlah_token': '49,000', 'usd': 'Tidak ada'}, {'nama': 'SafeUniverse... (SAFUV2)', 'symbol': 'SAFUV2', 'contract': '0xe2271046a181b41f20ad1a4076a4fa0fd0853d09', 'jumlah_token': '28,090,208.8628864', 'usd': 'Tidak ada'}, {'nama': 'Suntrust Fin... (SUNT)', 'symbol': 'SUNT', 'contract': '0x319bf3bb8ab93658074be595c4aa55cd60380af7', 'jumlah_token': '1,400', 'usd': 'Tidak ada'}, {'nama': 'TeaCrypto Fi... (TCF)', 'symbol': 'TCF', 'contract': '0xd78bd47a6934959583b47f081ce0f9fd5e0338d1', 'jumlah_token': '2,000,000', 'usd': 'Tidak ada'}, {'nama': 'TheEver.io (EVER)', 'symbol': 'EVER', 'contract': '0x5190b01965b6e3d786706fd4a999978626c19880', 'jumlah_token': '800,000', 'usd': 'Tidak ada'}, {'nama': 'TheVera.io (VERA)', 'symbol': 'VERA', 'contract': '0x0df62d2cd80591798721ddc93001afe868c367ff', 'jumlah_token': '800,000', 'usd': 'Tidak ada'}, {'nama': 'Ulink Financ... (ULK)', 'symbol': 'ULK', 'contract': '0x23481f4d3ac4642d2f45d014a514b45b0338b927', 'jumlah_token': '7,500,000', 'usd': 'Tidak ada'}, {'nama': 'Ultraman Tok... (UMAN)', 'symbol': 'UMAN', 'contract': '0xff3f9cc3083580bafd140e8f05cf2d7c3af15b53', 'jumlah_token': '479,900.00808616', 'usd': 'Tidak ada'}, {'nama': 'VANCAT Token (VANCAT)', 'symbol': 'VANCAT', 'contract': '0x8597ba143ac509189e89aab3ba28d661a5dd9830', 'jumlah_token': '41,523,853', 'usd': '$0.21'}, {'nama': 'VANCATDOG (VANCAT...)', 'symbol': 'VANCATDOG', 'contract': '0x97f4e15606cf335b7a6daec2ba02449fb5da69c6', 'jumlah_token': '150,000,000,000', 'usd': 'Tidak ada'}, {'nama': 'VDSB Token (VDSB)', 'symbol': 'VDSB', 'contract': '0x7322cc8b45cf8bda4b20cef958b873db7e8d570a', 'jumlah_token': '1,000,000', 'usd': 'Tidak ada'}, {'nama': 'VERGE (XVG)', 'symbol': 'XVG', 'contract': '0xad0be9ca7d2ec9cc1a5e423add66db60ea2d2329', 'jumlah_token': '1,000', 'usd': 'Tidak ada'}, {'nama': 'WAIVLENGTH (WAIV)', 'symbol': 'WAIV', 'contract': '0xaa5c91f3df88b8b3863d0899bca33e70482bed2a', 'jumlah_token': '1,240,189,208.55629', 'usd': 'Tidak ada'}, {'nama': 'Wall Street ... (WSG)', 'symbol': 'WSG', 'contract': '0xA58950F05FeA2277d2608748412bf9F802eA4901', 'jumlah_token': '500,000', 'usd': '$0.05'}, {'nama': 'wDogecoin (wDOGE)', 'symbol': 'wDOGE', 'contract': '0xf40c1f421ee02a550afdd8712ef34dce97eec6f2', 'jumlah_token': '300,000', 'usd': 'Tidak ada'}, {'nama': 'XMAGNET (XMAG)', 'symbol': 'XMAG', 'contract': '0xa9686056aa043e49d560fc4b0fd163ceef17d0c9', 'jumlah_token': '1.25', 'usd': 'Tidak ada'}, {'nama': 'YOOSHI (YOOSHI)', 'symbol': 'YOOSHI', 'contract': '0x02ff5065692783374947393723dba9599e59f591', 'jumlah_token': '10,000', 'usd': 'Tidak ada'}]

Polygon Scan
[{'nama': 'Apple Financ... (Apple)', 'symbol': 'Apple', 'contract': '0xda8f20bf431d04a3661250f922d75e2bbe0b001c', 'jumlah_token': '1.34', 'usd': 'Tidak ada'}, {'nama': 'Kommunitas (KOM)', 'symbol': 'KOM', 'contract': '0xc004e2318722ea2b15499d6375905d75ee5390b8', 'jumlah_token': '2,000', 'usd': 'Tidak ada'}, {'nama': 'MoonEdge (MOONED)', 'symbol': 'MOONED', 'contract': '0x7e4c577ca35913af564ee2a24d882a4946ec492b', 'jumlah_token': '9,425.65610088', 'usd': 'Tidak ada'}, {'nama': 'Plasma (PoS) (PPAY)', 'symbol': 'PPAY', 'contract': '0x08158a6b5d4018340387d1a302f882e98a8bc5b4', 'jumlah_token': '140', 'usd': 'Tidak ada'}, {'nama': 'XNFT001 (XNFT00...)', 'symbol': 'PPAY', 'contract': '0xd55cba0a336c1837ad3b8747efc1800de4fb00cd', 'jumlah_token': '140', 'usd': 'Tidak Ada'}]

[Program finished]
```
# PancakeSwap API for BinanceSmartChain (Bsc) 
This api refresh price always 5 minute

```Python
from libs.getprice import PancakeSwap
from blockchain.EtherBlock import BinanceSmartChain

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
  print(f"Name: {token_name}\nValues: {value_token} {symb}\nPancakeSwap Price: {bsc_market.getprice_BNB()}\r\n")
```
OUTPUT
```
Binance SmartChain Explorer
Name: DeFi For You... (DFY)
Values: 2.42 DFY
PancakeSwap Price: 0.0002915283299311617908843660320057

Name: Spore (SPORE)
Values: 2,920,837,050.80414 SPORE
PancakeSwap Price: 0.0000000000003139460655345544872405386104685

Name: Agrinoble (AGN)
Values: 10,900 AGN
PancakeSwap Price: Tidak Ada price_BNB

Name: ALPACAFIN.CO... (ALPACA)
Values: 28,102,000 ALPACA
PancakeSwap Price: 0.0000001867870353453604727112897002711

Name: Automata (ATA)
Values: 50 ATA
PancakeSwap Price: 0

Name: Baby Doge Co... (BabyDo...)
Values: 252,291,809.868527 BabyDoge
PancakeSwap Price: 0.000000000003873562911286853684584744679853

Name: Beer Money (BEER)
Values: 3 BEER
PancakeSwap Price: 0.00005641793837173952139084343897413

Name: BITCHIP (CHIP)
Values: 2,850,000,000 CHIP
PancakeSwap Price: 0

Name: BNBL TOKEN (BNBL)
Values: 50 BNBL
PancakeSwap Price: 0

Name: ChesterCoin (CTRFI)
Values: 14,766,732,003.9107 CTRFI
PancakeSwap Price: 0.00000000000002044491622101088392370074923166

Name: Corgi doge (CORGI)
Values: 105,000 CORGI
PancakeSwap Price: 0.000000002061532915214885479759148061752

Name: Crox Token (CROX)
Values: 2.25172299 CROX
PancakeSwap Price: 0.000305368632209768343105533760657

Name: Ether2 (ETHER2)
Values: 250,000,000 ETHER2
PancakeSwap Price: 0

Name: Fire Protoco... (FPF)
Values: 32 FPF
PancakeSwap Price: Tidak Ada price_BNB

Name: FishSwap (FISH)
Values: 11 FISH
PancakeSwap Price: 0

Name: GoFlux.io (FLUX)
Values: 950,000 FLUX
PancakeSwap Price: 0.000416409388845074495909908492078

Name: Gold Bee (GBE)
Values: 169.32302137 GBE
PancakeSwap Price: 0

Name: HelloSwap To... (HELLO)
Values: 5,200 HELLO
PancakeSwap Price: 0

Name: Investelly (INVEST...)
Values: 10 INVESTEL
PancakeSwap Price: 0.00001009484233635546445626634459038

Name: Koda Robot D... (KODA)
Values: 1,532,286.80001067 KODA
PancakeSwap Price: 0

Name: Lindalit BSC (LINDA)
Values: 0.00087591 LINDA
PancakeSwap Price: 0

Name: Lock Chain F... (LOCKCH...)
Values: 2,750,000 LOCKCHAIN
PancakeSwap Price: 0

Name: Medical Veda (MVEDA)
Values: 3,500,000 MVEDA
PancakeSwap Price: 0

Name: Minereum BSC (MNEB)
Values: 150,000 MNEB
PancakeSwap Price: 0.0002061517148775796939859801715223

Name: Moon Chain (MCF)
Values: 1,000,000 MCF
PancakeSwap Price: 0.000000000001711296200685053429767876006837

Name: Moon Stake (MSEF)
Values: 20,000 MSEF
PancakeSwap Price: 0

Name: Nyan Cat Tok... (NCAT)
Values: 42,529,631.3077643 NCAT
PancakeSwap Price: 0

Name: Poodledog To... (POODLE)
Values: 25 POODLE
PancakeSwap Price: 0

Name: SAFE MERCURY (SMRCY)
Values: 1,188,841.64349208 SMRCY
PancakeSwap Price: 0

Name: Safe Nebula (SNB)
Values: 250,000,000 SNB
PancakeSwap Price: 0

Name: SafeGas (SAFEGA...)
Values: 49,000 SAFEGAS
PancakeSwap Price: 0

Name: SafeUniverse... (SAFUV2)
Values: 28,090,208.8628864 SAFUV2
PancakeSwap Price: 0

Name: Suntrust Fin... (SUNT)
Values: 1,400 SUNT
PancakeSwap Price: 0

Name: TeaCrypto Fi... (TCF)
Values: 2,000,000 TCF
PancakeSwap Price: 0

Name: TheEver.io (EVER)
Values: 800,000 EVER
PancakeSwap Price: 0.000271976832668170770323726602572

Name: TheVera.io (VERA)
Values: 800,000 VERA
PancakeSwap Price: 0.000379399747873644752442549176166

Name: Ulink Financ... (ULK)
Values: 7,500,000 ULK
PancakeSwap Price: 0

Name: Ultraman Tok... (UMAN)
Values: 479,900.00808616 UMAN
PancakeSwap Price: 0.000000000144765487228508541018833519548

Name: VANCAT Token (VANCAT)
Values: 41,523,853 VANCAT
PancakeSwap Price: 0.00000000001196168722704529515043716690936

Name: VANCATDOG (VANCAT...)
Values: 150,000,000,000 VANCATDOG
PancakeSwap Price: 0

Name: VDSB Token (VDSB)
Values: 1,000,000 VDSB
PancakeSwap Price: 0

Name: VERGE (XVG)
Values: 1,000 XVG
PancakeSwap Price: Tidak Ada price_BNB

Name: WAIVLENGTH (WAIV)
Values: 1,240,189,208.55629 WAIV
PancakeSwap Price: 0.000000000001605406255338604963104782772103

Name: Wall Street ... (WSG)
Values: 500,000 WSG
PancakeSwap Price: 0.0000000002336748686073267023493636979548

Name: wDogecoin (wDOGE)
Values: 300,000 wDOGE
PancakeSwap Price: 0.0000000000122746988603025853240324256506

Name: XMAGNET (XMAG)
Values: 1.25 XMAG
PancakeSwap Price: 0

Name: YOOSHI (YOOSHI)
Values: 10,000 YOOSHI
PancakeSwap Price: 0.0000000003509754844784882040743473678856


Process finished with exit code 0
```

# Keterangan

0 = tidak ada liquidity yang tersedia pada token

Tidak Ada price_BNB = Token Belum di Approve

# Untuk hanya menginstall library
```Python
pip install EtherBlockchain
```
