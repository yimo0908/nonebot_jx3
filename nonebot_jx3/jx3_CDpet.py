import httpx
from PIL import ImageFont, ImageDraw, Image
from time import strftime, localtime
import datetime
from io import BytesIO
import base64


async def get_pet_time(server, name):
    api = 'https://next.jx3box.com/api/serendipity?server=' + server + '&role=&serendipity=' + \
          name + '&start=0&pageIndex=1&pageSize=1'
    async with httpx.AsyncClient() as s:
        res = await s.get(api)
        data = res.json()
        dictionary = data["data"]["data"]
        one_subject = ""
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


async def get_cdpet_pic(server):
    who = ["稻稻", "蟹仔", "蟹兵", "蟹卒", "蟹将", "蟹帅", "小灰", "小锦", "白鹅", "蟹相", "蟹象", "阿里", "阿飞",
           "蟹仕", "蟹士", "蟹炮", "蟹砲", "哈皮", "嘟嘟", "静静", "大头鹅", "蟹车·红", "蟹车·蓝", "蟹马·红", "蟹马·蓝"]
    title = f"{server}的蹲宠CD如下：\n"
    end = "\n统计时间：" + strftime("%Y-%m-%d %H:%M:%S",
                               localtime()) + "\n数据来源：茗伊插件集\nhttps://j3cx.com/serendipity"
    sendmsg = ""
    for name in who:
        sendmsg += await get_pet_time(server, name) + "\n"
    msg = title + sendmsg + end
    img = Image.new('RGB', (700, 1100), (255, 255, 255))
    font_path = "font.ttc"
    font = ImageFont.truetype(font_path, 32)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), msg, font=font, fill=(0, 0, 0))
    output_buffer = BytesIO()
    img.save(output_buffer, format='PNG')
    base64_code = base64.b64encode(output_buffer.getvalue()).decode()
    return f"[CQ:image,file=base64://{base64_code}]"
