import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

async def test(loop):
        await orm.create_pool(loop = loop,host='localhost', port =3306, user='root', password='1111', db='awesome')
        u = User(name='Test', email='test@example.com1', passwd='1234567890', image='about:blank', id="1231")
        await u.save()

loop.run_until_complete(test(loop))
loop.close()

