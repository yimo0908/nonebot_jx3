import httpx
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='8', misfire_grace_time=2)
async def _():
    bot = nonebot.get_bot()
    api = f'https://jx3api.com/api/daily.php?token=153166341&server=绝代天骄'
    try:
        res = httpx.get(api)
        dictionary = res.json()
        msg = ''
        for key in dictionary:
            msg += "%s: %s\n" % (key, dictionary[key])
        msg = msg[:-1]
        await bot.send_group_msg(group_id=1003245549, message=f'今日日常：\n{msg}')
    except CQHttpError:
        pass
