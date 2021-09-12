import httpx


async def get_daily_report():
    api = f'https://jx3api.com/app/daily?server=all'
    async with httpx.AsyncClient() as s:
        try:
            res = await s.get(api)
            dictionary = res.json()['data']
            msg = (
                "今天是{DateTime}，周{Week}\n大战：{DayWar}\n矿车：{DayCamp}\n战场：{DayBattle}\n驰援：{DayCommon}\n周常公共：{WeekCommon}\n周常小队：{WeekFive}\n周常团队：{WeekTeam}".format(
                    **dictionary))
            if "DayDraw" in dictionary.keys():
                li = dictionary['DayDraw']
                msg2 = "\n美人图：\n"
                for i, subject in enumerate(li):
                    one_subject = "%s : %s" % (subject['server'], subject['draw'])
                    if i != len(li) - 1:
                        msg2 += one_subject + ";\n"
                    else:
                        msg2 += one_subject + "。"
            msg = msg + msg2.replace("'", "").replace("长安城, 天鹅坪, 蝶恋花, 破阵子, 龙争虎斗, 剑胆琴心, 乾坤一掷, 唯我独尊, 幽月轮", "大部分").replace(
                "梦江南, 斗转星移, 飞龙在天, 青梅煮酒", "双梦|青梅|姨妈|飞龙")
            return "\n今日日常：\n" + msg
        except Exception as e:
            msg = str(e)
            return "消息处理失败" + msg
