import typing
from aiohttp import ClientSession, ClientResponse

from .exceptions import PastebinError


class PastebinBase:
    _base_url = ''

    @property
    def _post_url(self):
        return self._base_url + 'documents'

    def __init__(self, session: ClientSession = None):
        self._session = session or ClientSession()

    async def create_paste_from_text(self, text: str):
        return self._base_url

    async def create_paste_from_file(self, file: typing.TextIO):
        text = file.read()
        return await self.create_paste_from_text(text)

    @classmethod
    def _validate_response(cls, r: ClientResponse):
        if r.status != 200:
            raise PastebinError(cls.__name__, r.status)
        return r

    async def disconnect(self):
        await self._session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()


class BadRequest(Exception):
    def __init__(self, txt=None):
        self.txt = txt
