import httpx
import json
import os
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
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


who1 = {
    "哈皮", "嘟嘟", "小灰", "小锦", "白鹅", "稻稻", "蟹仔", "蟹仕", "蟹兵", "蟹卒", "蟹士", "蟹将", "蟹帅", "蟹炮", "蟹相", "蟹砲", "蟹象", "阿里", "阿飞",
    "静静"
}
who2 = {
    "大头鹅",
    "蟹车·红",
    "蟹车·蓝",
    "蟹马·红",
    "蟹马·蓝",
}
time = "\n统计时间：" + strftime("%Y-%m-%d %H:%M:%S", localtime())
title = "绝代天骄的蹲宠CD如下：\n"

sendmsg1 = ""
for i in who1:
    sendmsg1 += get_msg(i) + "\n"

sendmsg2 = ""
for i in who2:
    sendmsg2 += get_msg(i) + "\n"

msg = title + sendmsg1 + sendmsg2 + time
bk_img = cv2.imread("hoshino/modules/nonebot_jx3/bk.png")
#设置需要显示的字体
fontpath = "hoshino/modules/nonebot_jx3/font.ttc"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
#绘制文字信息
draw.text((10, 10), msg, font=font, fill=(0, 0, 0))
bk_img = np.array(img_pil)
cv2.imwrite("dunchong.jpg", bk_img)

root = os.getcwd()

@on_command('蹲宠', only_to_me=False)
async def jx3_CDpet(session):
    await session.send(f"[CQ:image,file=file:///{root}//dunchong.jpg]")