# BinanceSmartChain API

Api yang sengaja dibuat untuk mengambil Info Token dari BlockChain BinanceChain, yang sangat simple
untuk digunakan. Price diambel berdasarkan Price USDT Yang tersedia dalam Blockchain BSC sendiri "Jika ada" 
# Example

```python
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

```
output

```
[{'nama': 'Binance-Peg ... (BSC-US...)', 'symbol': 'BSC-USD', 'contract': '0x55d398326f99059ff775485246999027b3197955', 'jumlah_token': '7.52540758', 'usd': '$7.48', 'price_bnb': '0.003232440890598071417058868717118'}, {'nama': 'PancakeSwap ... (Cake)', 'symbol': 'Cake', 'contract': '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82', 'jumlah_token': '0.00919106', 'usd': '$0.13', 'price_bnb': '0.0466340293589923063671123330144'}, {'nama': 'Baby Doge Co... (BabyDo...)', 'symbol': 'BabyDoge', 'contract': '0xc748673057861a797275CD8A068AbB95A902e8de', 'jumlah_token': '882.27314237', 'usd': '$0.00', 'price_bnb': '0.000000000004932845028531061597904267225273'}, {'nama': 'BSCS Token (BSCS)', 'symbol': 'BSCS', 'contract': '0xbcb24afb019be7e93ea9c43b7e22bb55d5b7f45d', 'jumlah_token': '4.69477766', 'usd': '$0.49', 'price_bnb': '0.000336032208209802629277280605301'}, {'nama': 'FaraCrystal (FARA)', 'symbol': 'FARA', 'contract': '0xf4ed363144981d3a65f42e7d0dc54ff9eef559a1', 'jumlah_token': '2.00184691', 'usd': '$9.17', 'price_bnb': '0.01386655983676446039536927920576'}, {'nama': 'Harp Coin (HARP)', 'symbol': 'HARP', 'contract': '0xe37ab1f60987cb4ac3c27918c11412f41460ab0b', 'jumlah_token': '1,764,689.40927999', 'usd': 'Tidak ada', 'price_bnb': '0.0000000000001870876592864405152507860645874'}, {'nama': 'Lunar (LUNAR)', 'symbol': 'LUNAR', 'contract': '0xf4206e5F264420630520e0D23c14D8Dd5645e6C3', 'jumlah_token': '1,906.94269768', 'usd': 'Tidak ada', 'price_bnb': '0.0000004346426287440354014105888813505'}, {'nama': 'MDX Token (MDX)', 'symbol': 'MDX', 'contract': '0x9c65ab58d8d978db963e63f2bfb7121627e3a739', 'jumlah_token': '2.28206661', 'usd': 'Tidak ada', 'price_bnb': '0.00342928983743084787848057784475'}, {'nama': 'Minereum BSC (MNEB)', 'symbol': 'MNEB', 'contract': '0xd22202d23fe7de9e3dbe11a2a88f42f4cb9507cf', 'jumlah_token': '150,000', 'usd': 'Tidak ada', 'price_bnb': '0.00037575839718806974622491269986'}, {'nama': 'Mobox (MBOX)', 'symbol': 'MBOX', 'contract': '0x3203c9e46ca618c8c1ce5dc67e7e9d75f5da2377', 'jumlah_token': '1.35232942', 'usd': '$2.16', 'price_bnb': '0.005026258436941619561711045248874'}, {'nama': 'Pancake LPs (Cake-L...)', 'symbol': 'Cake-LP', 'contract': '0xffd50f49ad4f9335abc1f1b9e5a6ed90815f5fda', 'jumlah_token': '0.09652488', 'usd': 'Tidak ada', 'price_bnb': 'Tidak Ada price_BNB'}, {'nama': 'PING (PING)', 'symbol': 'PING', 'contract': '0x5546600f77eda1dcf2e8817ef4d617382e7f71f5', 'jumlah_token': '269.38205122', 'usd': '$1.17', 'price_bnb': '0.00001365010481415920949406494868366'}, {'nama': 'Position (POSI)', 'symbol': 'POSI', 'contract': '0x24aefaddbaec40b5e6912b0200164b51c5b17181', 'jumlah_token': '0.0001', 'usd': 'Tidak ada', 'price_bnb': '0.000000311407266455613788200177224745'}, {'nama': 'YooShi Frien... (YSNFT)', 'symbol': 'POSI', 'contract': '0x32afc8dc2ff4af284fa5341954050f917357a5f1', 'jumlah_token': '0.0001', 'usd': 'Tidak Ada', 'price_bnb': 'Tidak Ada price_BNB'}]

[Program finished]
```
untuk nilai yang ada pada 'price_bnb' diambil dari Api PancakeSwap, perubahan data price diambil setiap 5 menit.

