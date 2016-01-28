import asyncio
import time
from urllib.parse import urlencode
from urllib.request import urlopen


class SlackRequest(object):
    def __init__(self):
        pass

    @asyncio.coroutine
    def do(self, token, request="?", post_data={}, domain="slack.com"):
        post_data["token"] = token
        post_data = urlencode(post_data)
        url = 'https://{}/api/{}'.format(domain, request)
        loop = asyncio.get_event_loop()
        res = yield from loop.run_in_executor(
            None, urlopen, url, post_data.encode('utf-8'))
        return res

