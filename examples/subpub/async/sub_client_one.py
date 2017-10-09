import asyncio
import time
import zmq.asyncio
from zmq.asyncio import Context


zmq.asyncio.install()

ctx = zmq.asyncio.Context()

async def recv():
    s = ctx.socket(zmq.SUB)
    s.connect('tcp://127.0.0.1:5555')
    s.subscribe(b'')
    while True:
        msg = await s.recv_multipart()
        print('received', msg)
        time.sleep(5)
    s.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(recv())
loop.close()
