import httpx
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='8', misfire_grace_time=2)
async def _():
    bot = nonebot.get_bot()
    api = f'https://jx3api.com/app/getDaily?server=绝代天骄'
    try:
        res = httpx.get(api)
        dictionary = res.json()['data']
        msg = ("今天是{Date}，周{Week}\n大战：{DayWar}\n战场：{DayBattle}\n驰援：{DayCommon}\n周常公共：{WeekCommon}\n周常小队：{WeekFive}\n周常团队：{WeekTeam}".format(**dictionary))
        if "DayDraw" in dictionary.keys():
            msg += ("\n美人图：{DayDraw}".format(**dictionary))
        await bot.send_group_msg(group_id=1003245549, message=f'今日日常：\n{msg}')
    except CQHttpError:
        pass
