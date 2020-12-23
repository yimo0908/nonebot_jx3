from nonebot import on_command
import httpx
import json


@on_command('沙盘', only_to_me=False)
async def jx3_sand(session):
    user = session.event.user_id
    api = f'https://jx3api.com/next/sand.php?token=jx3zhenhaowan&server=%E7%BB%9D%E4%BB%A3%E5%A4%A9%E9%AA%84'
    res = httpx.get(api)
    dictionary = json.loads(res.content)
    image_url = dictionary["data"]["url"]
    await session.send(f'[CQ:at,qq={user}]' + f'[CQ:image,file={image_url}]')