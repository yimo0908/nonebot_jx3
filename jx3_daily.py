from nonebot import on_command
import httpx


@on_command('日常', only_to_me=False)
async def jx3_daily(session):
    user = session.event.user_id
    fwq = "绝代天骄"
    api = f'https://jx3api.com/next/daily.php?token=jx3zhenhaowan&server={fwq}'
    async with httpx.Client() as s:
        try:
            res = await s.get(api)
        except Exception as e:
            msg = str(e)
            # print(msg)
            await session.send(f'[CQ:at,qq={user}]' + '消息处理失败\n' + msg)
            return

    dictionary = res.json()
    msg = ''
    for key in dictionary:
        msg += "%s: %s\n" % (key, dictionary[key])
    # print(msg)
    await session.send(f'[CQ:at,qq={user}]' + "今日日常：\n" + msg)
