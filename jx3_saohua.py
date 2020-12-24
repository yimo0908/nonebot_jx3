from nonebot import on_command
import httpx
import json


@on_command('骚话', only_to_me=False)
async def jx3_sanhua(session):
    api = f'https://jx3api.com/next/random.php?token=jx3zhenhaowan'
    res = httpx.get(api)
    dictionary = json.loads(res.content)
    await session.send(dictionary["data"]["text"])