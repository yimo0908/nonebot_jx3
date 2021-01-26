import httpx
import json
import os
from PIL import ImageFont, ImageDraw, Image
from time import strftime, localtime
import datetime
from nonebot import on_command


def get_pet_time(name):
    api = 'https://next.jx3box.com/api/serendipity?server=绝代天骄&role=&serendipity=' + \
          name + '&start=0&pageIndex=1&pageSize=1'
    res = httpx.get(api)
    data = json.loads(res.content)
    dictionary = data["data"]["data"]
    for _, subject in enumerate(dictionary):
        _time = datetime.datetime.strptime(
            subject["date_str"], '%Y-%m-%d %H:%M:%S')
        _time = datetime.datetime.now() - _time
        mm, ss = divmod(_time.seconds, 60)
        hh, mm = divmod(mm, 60)
        s = "%dh %02dm %02ds" % (hh, mm, ss)
        if _time.days:
            def plural(n):
                return n, abs(n) != 1 and "s" or ""
            s = ("%d d%s  " % plural(_time.days)) + s
        one_subject = "%s              上个CD：%s前" % (subject["serendipity"], s)
    return one_subject


@on_command('蹲宠', only_to_me=False)
async def jx3_CDpet(session):
    who = ["稻稻", "蟹仔", "蟹兵", "蟹卒", "蟹将", "蟹帅", "小灰", "小锦", "白鹅", "蟹相", "蟹象", "阿里", "阿飞",
           "蟹仕", "蟹士", "蟹炮", "蟹砲", "哈皮", "嘟嘟", "静静", "大头鹅", "蟹车·红", "蟹车·蓝", "蟹马·红", "蟹马·蓝"]
    title = "绝代天骄的蹲宠CD如下：\n"
    end = "\n统计时间：" + strftime("%Y-%m-%d %H:%M:%S",
                               localtime()) + "\n数据来源：茗伊插件集\nhttps://j3cx.com/serendipity"
    sendmsg = ""
    for name in who:
        sendmsg += get_pet_time(name) + "\n"
    msg = title + sendmsg + end
    img = Image.new('RGB', (700, 1100), (255, 255, 255))
    # 设置需要显示的字体
    font_path = "font.ttc"
    font = ImageFont.truetype(font_path, 32)
    draw = ImageDraw.Draw(img)
    # 绘制文字信息
    draw.text((10, 10), msg, font=font, fill=(0, 0, 0))
    img.save("dunchong.jpg", 'jpeg')
    root = os.getcwd()
    await session.send(f"[CQ:image,file=file:///{root}\\dunchong.jpg]")
