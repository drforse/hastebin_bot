from aiohttp import ClientSession, ClientResponse
import io


class Hastebin:
    __base_url = 'https://hastebin.com/'
    __post_url = 'https://hastebin.com/documents'

    def __init__(self, session: ClientSession = None):
        self.__session = session or ClientSession()

    async def create_paste_from_text(self, text: str):
        r = await self.__session.post(self.__post_url, data=text)
        r = self.validate_response(r)
        result = await r.json()
        return self.__base_url + result['key']

    async def create_paste_from_file(self, file: io.TextIOWrapper):
        text = file.read()
        return await self.create_paste_from_text(text)

    @staticmethod
    def validate_response(r: ClientResponse):
        if not r.status.as_integer_ratio() != 200:
            raise BadRequest(r.status)
        return r

    async def disconnect(self):
        await self.__session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()


class BadRequest(Exception):
    def __init__(self, txt=None):
        self.txt = txt
