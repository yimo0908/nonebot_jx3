from nonebot import on_command

import httpx
import json


@on_command('日常', only_to_me=False)
async def jx3_daily(session):
    user = session.event.user_id
    fwq = "绝代天骄"
    api = f'https://jx3api.com/next/daily.php?token=jx3zhenhaowan&server={fwq}'
    res = httpx.get(api)
    dictionary = json.loads(res.content)
    if "美人画像" not in dictionary.keys():
        sendmsg = ("时间：{时间} 周{星期}\n大战：{秘境大战}\n战场：{今日战场}\n驰援：{驰援任务}\n周常公共任务：{武林通鉴·公共任务}\n周常5人本：{武林通鉴·秘境任务}\n周常10人本：{武林通鉴·团队秘境}".format(**dictionary))
    else:
        sendmsg = ("时间：{时间} 周{星期}\n大战：{秘境大战}\n战场：{今日战场}\n驰援：{驰援任务}\n美人图：{美人画像}\n周常公共任务：{武林通鉴·公共任务}\n周常5人本：{武林通鉴·秘境任务}\n周常10人本：{武林通鉴·团队秘境}".format(**dictionary))
    await session.send(f'[CQ:at,qq={user}]' + "今日日常：\n" + sendmsg)
