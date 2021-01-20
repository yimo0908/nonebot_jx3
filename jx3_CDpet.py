import httpx
import json
from time import strftime, localtime
from nonebot import on_command


def get_msg(what):
    api = 'https://next.jx3box.com/api/serendipity?server=绝代天骄&role=&serendipity=' + \
        what+'&start=0&pageIndex=1&pageSize=1'
    res = httpx.get(api)
    data = json.loads(res.content)
    dictionary = data["data"]["data"]
    for i,subject in enumerate(dictionary):
        one_subject = "%s  上个CD：%s" % (
            subject["serendipity"], subject["date_str"])
    return one_subject


who = {"哈皮", "嘟嘟", "大头鹅", "小灰", "小锦", "白鹅", "稻稻", "蟹仔", "蟹仕", "蟹兵", "蟹卒", "蟹士", "蟹将",
       "蟹帅", "蟹炮", "蟹相", "蟹砲", "蟹象", "蟹车·红", "蟹车·蓝", "蟹马·红", "蟹马·蓝", "阿里", "阿飞", "静静"}

time = "\n统计时间："+strftime("%Y-%m-%d %H:%M:%S", localtime())
title = "绝代天骄的蹲宠CD如下：\n"

sendmsg = ""
for i in who:
    sendmsg += get_msg(i) + "\n"

# print(title+sendmsg+time)
@on_command('蹲宠', only_to_me=False)
async def jx3_CDpet(session):
    await session.send(title+sendmsg+time)
