import httpx


def get_id(name):
    api = f'https://helper.jx3box.com/api/item/search?keyword={name}'
    res = httpx.get(api)
    li = res.json()["data"]["data"]
    item_info = li[0]
    item_id = item_info['id']
    return item_id


async def get_price(name):
    item_id = get_id(name)
    api = f'https://helper.jx3box.com/api/item/{item_id}/prices?server=绝代天骄&limit=15 '
    async with httpx.AsyncClient() as sess:
        try:
            res = await sess.get(api)
            if res.json()["code"] == 200:
                li = res.json()["data"]["prices"]
                sever = li[0]["server"]
                string = ""
                for i, subject in enumerate(li):
                    Up = round(subject["unit_price"] / 10000, 2)
                    Np = round(subject["n_money"] / 10000, 2)
                    one_subject = "%s金 * %s  =   %s金" % (Up, subject["n_count"], Np)
                    if i != len(li) - 1:
                        string += one_subject + ";\n"
                report = f"{sever} 的 {name} 数据如下：\n" + string
                return report
            else:
                return '消息处理失败，请检查输入的服务器名称是否正确！'
        except Exception as e:
            return "消息处理失败" + str(e)
