import httpx
import json
from time import strftime, localtime
api = f'https://next.jx3box.com/api/serendipity?server=绝代天骄&role=&serendipity=故园风雨&start=0&pageIndex=1&pageSize=10'
res = httpx.get(api)
data = json.loads(res.content)
dictionary = data["data"]["data"]
sendmsg2 = ""
for i, subject in enumerate(dictionary):
    one_subject = "%s：%s" % (
        subject["name"], subject["date_str"])
    if i != len(dictionary) - 1:
        sendmsg2 += one_subject + ";\n"
    else:
        sendmsg2 += one_subject + "。"
sendmsg1 = ""
for i, subject in enumerate(dictionary):
    one_subject = "%s最近10个%s记录为：\n" % (
        subject["server"], subject["serendipity"])
sendmsg1 += one_subject
sendmsg3 = "\n\n统计时间："+strftime("%Y-%m-%d %H:%M:%S", localtime())
print(sendmsg1+sendmsg2+sendmsg3)
