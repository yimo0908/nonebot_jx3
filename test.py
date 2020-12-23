import httpx
import json
api = f'https://jx3api.com/next/daily.php?token=jx3zhenhaowan&server=%E7%BB%9D%E4%BB%A3%E5%A4%A9%E9%AA%84'
res = httpx.get(api)
dictionary = json.loads(res.content)
weekday = ("{星期}".format(**dictionary))
if weekday == ("一" or "二" or "四"):
    sendmsg = ("时间：{时间} 周{星期}\n大战：{秘境大战}\n战场：{今日战场}\n驰援：{驰援任务}\n周常公共任务：{武林通鉴·公共任务}\n周常5人本：{武林通鉴·秘境任务}\n周常10人本：{武林通鉴·团队秘境}".format(**dictionary))
else:
    sendmsg = ("时间：{时间} 周{星期}\n大战：{秘境大战}\n战场：{今日战场}\n驰援：{驰援任务}\n美人图：{美人画像}\n周常公共任务：{武林通鉴·公共任务}\n周常5人本：{武林通鉴·秘境任务}\n周常10人本：{武林通鉴·团队秘境}".format(**dictionary))
print(sendmsg)
