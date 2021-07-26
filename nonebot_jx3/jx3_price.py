import httpx


async def request(url):
    async with httpx.AsyncClient() as client:
        data = await client.get(url)
        result = data.json()
        await client.aclose()
        return result


async def handle_item_name(item_name):
    item_name = item_name.replace("(", "（").replace(")", "）")
    if item_name.endswith("五行石"):
        item_name = "五行石（" + item_name[0] + "级）"
    if item_name.endswith("五彩石"):
        item_name = item_name[0].replace("三", "叁").replace("四", "肆").replace("五", "伍").replace("六", "陆") + "级五彩石"
    if item_name == "赤阳金":
        item_name = "赤阳金碎片"
    return item_name


async def get_id(name):
    name = await handle_item_name(name)
    dic = {"宝石": "5_30828", "露水": "5_30840", "玛瑙": "5_30846", "五色石": "5_36472", "沉香木": "5_30855", "猫眼石": "5_30852",
           "铜矿": "5_30674", "铁矿": "5_30677", "杂碎": "5_30682", "鱼肉": "5_30827", "碎肉": "5_30823", "血": "5_30825",
           "骨头": "5_30826", "彼岸花": "5_30838", "珊瑚": "5_30839", "虫草": "5_30836", "芍药": "5_30837", "甘草": "5_30830",
           "大黄": "5_30831", "千里香": "5_30832", "枸杞": "5_30833", "川贝": "5_30834", "五味子": "5_30835"
           }
    if name in dic:
        item_id = dic.get(name)
    else:
        data = await request(f'https://helper.jx3box.com/api/item/search?keyword={name}')
        li = data["data"]["data"]
        item_info = li[0]
        item_id = item_info['id']
    return item_id


async def get_price(name):
    item_id = await get_id(name)
    api = f'https://helper.jx3box.com/api/item/{item_id}/prices?server=绝代天骄&limit=15 '
    try:
        res = await request(api)
        if res["code"] == 200:
            li = res["data"]["prices"]
            sever = li[0]["server"]
            item_name = res["data"]["item"]["Name"]
            string = ""
            for i, subject in enumerate(li):
                Up = round(subject["unit_price"] / 10000, 2)
                Np = round(subject["n_money"] / 10000, 2)
                one_subject = "%s金 * %s  =   %s金" % (Up, subject["n_count"], Np)
                if i != len(li) - 1:
                    string += one_subject + ";\n"
            report = f"{sever} 的 {item_name} 交易数据如下：\n" + string
            return report
        else:
            return '消息处理失败，请检查输入的物品名称是否正确！'
    except Exception as e:
        return "消息处理失败" + str(e)
