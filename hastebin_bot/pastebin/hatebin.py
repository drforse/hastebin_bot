from .base import PastebinBase


class Hatebin(PastebinBase):
    _base_url = 'https://hatebin.com/'

    async def create_paste_from_text(self, text: str):
        r = await self._session.post(self._post_url, data={'text': text})
        r = self._validate_response(r)
        result = (await r.text()).strip()
        return self._base_url + result
