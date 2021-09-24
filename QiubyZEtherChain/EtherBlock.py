from QiubyZEtherChain.libs import RequestOveride

class EtherBlock(RequestOveride.Blockchain):
    def __init__(self, url):
        super(EtherBlock, self).__init__(url_parse=url)
        self.__tokenize = {"wallet": url.split("/")[-1], "token": []}
        self.__get_table_token()

    def gettotal(self):
        return (len(self.__tokenize.get("token")))

    def getJson(self):
        return self.__tokenize

    def getWallet(self):
        return self.__tokenize.get("wallet")

    def getToken(self):
        return self.__tokenize.get("token")

    def __get_table_token(self):
        listtoken = self._get_parser().find("ul", {"class": "list list-unstyled mb-0"})
        if(listtoken):
            token_list = listtoken.find_all_next("a", {"class":"link-hover d-flex justify-content-between align-items-center"})
            for i in range(len(token_list)):
                price = token_list[i].find("span", {"class": "list-usd-value d-block"})
                if (price):
                    price = price.text if price.text != "\xa0" else "Tidak ada"
                else:
                    price = "Tidak Ada"
                contract_token = token_list[i]["href"].split("?")[0].replace("/token/", "")
                token_info = token_list[i].find("span", {"class": "list-amount link-hover__item hash-tag hash-tag--md text-truncate"})
                if (token_info):
                    token_value, symbl = token_info.text.split(" ")
                Token_name = token_list[i].find("span", {"class": "list-name hash-tag text-truncate"}).text
                format_save = {
                        "nama": f"{Token_name}",
                        "symbol": f"{symbl}",
                        "contract": f"{contract_token}",
                        "jumlah_token": f"{token_value}",
                        "usd": f"{price}"
                }
                self.__tokenize.get("token").append(format_save)

class PolygonScan(EtherBlock):
    def __init__(self, address_wallet):
        super(PolygonScan, self).__init__(f"https://polygonscan.com/address/{address_wallet}")

class BinanceSmartChain(EtherBlock):
    def __init__(self, address_wallet):
        super(BinanceSmartChain, self).__init__(f"http://bscscan.com/address/{address_wallet}")

class Ethereum(EtherBlock):
    def __init__(self, address_wallet):
        super(Ethereum, self).__init__(f"https://etherscan.io/address/{address_wallet}")