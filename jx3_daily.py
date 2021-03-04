from nonebot import on_command
import httpx


@on_command('日常', only_to_me=False)
async def jx3_daily(session):
    user = session.event.user_id
    fwq = "绝代天骄"
    api = f'https://nico.nicemoe.cn/app/getDaily?server={fwq}'
    async with httpx.AsyncClient() as s:
        try:
            res = await s.get(api)
            dictionary = res.json()['data']
            msg = ("今天是{Date}，周{Week}\n大战：{DayWar}\n战场：{DayBattle}\n驰援：{DayCommon}\n周常公共：{WeekCommon}\n周常小队：{WeekFive}\n周常团队：{WeekTeam}".format(**dictionary))
            if "DayDraw" in dictionary.keys():
                msg += ("\n美人图：{DayDraw}".format(**dictionary))
            await session.send(f'[CQ:at,qq={user}]' + "\n今日日常：\n" + msg)
        except Exception as e:
            msg = str(e)
            # print(msg)
            await session.send(f'[CQ:at,qq={user}]' + "\n消息处理失败\n" + msg)