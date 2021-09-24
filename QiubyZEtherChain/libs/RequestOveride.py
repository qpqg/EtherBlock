from bs4 import BeautifulSoup as Parser
from requests import Session
class Blockchain(Session):
    def __init__(self, **kwargs):
        super(Blockchain, self).__init__()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
        self._block_chain = kwargs.get("url_parse")

    def _get_parser(self):
        parser = Parser(self.get(self._block_chain).text, "html.parser")
        return parser