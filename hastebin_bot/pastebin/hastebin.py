from .base import PastebinBase


class Hastebin(PastebinBase):
    _base_url = 'https://www.toptal.com/developers/hastebin/'

    async def create_paste_from_text(self, text: str):
        r = await self._session.post(self._post_url, data=text)
        r = self._validate_response(r)
        result = await r.json()
        return self._base_url + result['key']
