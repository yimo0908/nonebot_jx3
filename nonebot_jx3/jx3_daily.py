import httpx


async def get_daily_report():
    api = f'https://jx3api.com/app/daily?server=绝代天骄'
    async with httpx.AsyncClient() as s:
        try:
            res = await s.get(api)
            dictionary = res.json()['data']
            msg = (
                "今天是{DateTime}，周{Week}\n大战：{DayWar}\n矿车：{DayCamp}\n战场：{DayBattle}\n驰援：{DayCommon}\n周常公共：{"
                "WeekCommon}\n周常小队：{ ""WeekFive}\n周常团队：{WeekTeam}".format(**dictionary))
            if "DayDraw" in dictionary.keys():
                msg += ("\n美人图：{DayDraw}".format(**dictionary))
            return "\n今日日常：\n" + msg
        except Exception as e:
            msg = str(e)
            return "\n消息处理失败\n" + msg
