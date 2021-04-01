import httpx
from aiocqhttp.exceptions import Error as CQHttpError


async def scheduled_daily_report():
    api = f'https://jx3api.com/app/getDaily?server=绝代天骄'
    try:
        res = httpx.get(api)
        dictionary = res.json()['data']
        msg = ("今天是{Date}，周{Week}\n大战：{DayWar}\n战场：{DayBattle}\n驰援：{DayCommon}\n周常公共：{WeekCommon}\n周常小队：{"
               "WeekFive}\n周常团队：{WeekTeam}".format(**dictionary))
        if "DayDraw" in dictionary.keys():
            msg += ("\n美人图：{DayDraw}".format(**dictionary))
        return msg
    except CQHttpError:
        pass
