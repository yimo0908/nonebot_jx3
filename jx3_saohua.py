from nonebot import on_command
import httpx
import json


@on_command('骚话', only_to_me=False)
async def jx3_sanhua(session):
    api = f'https://www.nonebot.cn/next/random.php?token=153166341'
    async with httpx.AsyncClient() as sess:
        res = sess.get(api)
    dictionary = res.json()
    await session.send(dictionary["data"]["text"])
