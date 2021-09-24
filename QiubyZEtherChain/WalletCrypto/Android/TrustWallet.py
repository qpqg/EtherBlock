from subprocess import Popen, PIPE, STDOUT

class Terminal(Popen):
    def __init__(self, exec):
        super(Terminal, self).__init__(
            args=exec,
            shell=True,
            stderr=STDOUT,
            stdout=PIPE
        )
        self.communicate()

# class deeplink untuk memanggil TrusWallet
class TrustWallet(object):
    def __init__(self, **kwargs):
        self.__url_deep_link = "https://link.trustwallet.com/"
        self.__coin_id = kwargs.get("coin_id") or 20000714
        self.__contracaddress = kwargs.get("contractaddress")
        self.package = "com.wallet.crypto.trustapp"

    def getCoin_id(self):
        return self.__coin_id

    def getContractAddress(self, x):
        return self.__contracaddress

    def setCoin_id(self, x):
        self.__coin_id = x

    def setContractAddress(self, x):
        self.__coin_id = x

    def __exec(self, deeplink):
        return Terminal(f"am start -a android.intent.action.VIEW -d {repr(deeplink)}")

    def openBrowser(self, dapps):
        return self.__exec(f"{self.__url_deep_link}open_url?coin_id={self.__coin_id}&url={dapps}")

    def openCoin(self):
        return self.__exec(f"{self.__url_deep_link}open_coin?asset={self.__coin_id}")

    def addAsset(self):
        return self.__exec(f"{self.__url_deep_link}add_asset?asset=c{self.__coin_id}_t{self.__contracaddress}")
