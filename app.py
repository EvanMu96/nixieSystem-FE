#-*-coding:utf-8-*-
#author: Evan Mu
import logging; logging.basicConfig(level=logging.info)

import asyncio, os, json, time,
from datetime import datetime

from aiohttp import web

#index for webapp
@asyncio.coroutine
def index(request):
    return web.Response(body=bytes('<h1>Awesome</h1>'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()