from nonebot import on_command
import httpx


@on_command('骚话', only_to_me=False)
async def jx3_sanhua(session):
    api = f'https://jx3api.com/app/getRandom'
    res = httpx.get(api)
    dictionary = res.json()
    await session.send(dictionary["data"]["text"])
