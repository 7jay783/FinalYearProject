from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from os import path

DB_URL = f"mongodb://admin:07860@linux.vm/?retryWrites=true&w=majority"

DB = AsyncIOMotorClient(DB_URL)['final-year-project']

children = DB['children']


async def insert():
	c = await children.insert_one({'FaceId': 100,'type': 'test', 'info': {}})
	x = path.join('a', str(c.inserted_id))
	print(x)

loop = asyncio.get_event_loop()
loop.run_until_complete(insert())






