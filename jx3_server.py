from nonebot import on_command
import httpx
import json


@on_command('开服', only_to_me=False)
async def jx3_server(session):
    user = session.event.user_id
    fwq = "绝代天骄"
    api = f'https://jx3api.com/next/server.php?token=jx3zhenhaowan&server={fwq}'
    res = httpx.get(api)
    dictionary = json.loads(res.content)
    if dictionary["data"]["status"] == 1:
        await session.send(f'[CQ:at,qq={user}]' + dictionary["data"]["server"] + "已开服")
    else:
        await session.send(f'[CQ:at,qq={user}]' + dictionary["data"]["server"] + "未开服")
