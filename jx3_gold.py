from nonebot import on_command
import httpx
import json


@on_command('金价', only_to_me=False)
async def jx3_gold(session):
    user = session.event.user_id
    fwq="绝代天骄"
    api = f'https://jx3api.com/next/gold.php?token=jx3zhenhaowan&server={fwq}'
    res = httpx.get(api)
    dictionary = json.loads(res.content)
    qufu = dictionary["data"]["server"]
    wbl = dictionary["data"]["wanbaolou"]
    ym = dictionary["data"]["youmu"]
    uu = dictionary["data"]["uu898"]
    dd = dictionary["data"]["dd373"]
    wyqs = dictionary["data"]["5173"]
    qbby = dictionary["data"]["7881"]
    sendmsg = qufu+"的金价：\n万宝楼："+wbl+"\n游募："+ym+"\nuu898：" + \
        uu+"\ndd373："+dd+"\n5173："+wyqs+"\n7881："+qbby
    await session.send(f'[CQ:at,qq={user}]' + "\n" + sendmsg)
