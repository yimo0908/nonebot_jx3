import httpx


async def check_server(server):
    api = f'https://jx3api.com/app/check?server={server}'
    async with httpx.AsyncClient() as sess:
        try:
            res = await sess.get(api)
            dictionary = res.json()
            if dictionary['code'] == 200:
                if dictionary["data"]["status"] == 1:
                    msg = dictionary["data"]["region"] + dictionary["data"]["server"] + "已开服"
                else:
                    msg = dictionary["data"]["region"] + dictionary["data"]["server"] + "未开服"
                return msg
            else:
                return '消息处理失败，请检查输入的服务器名称是否正确！'
        except Exception as e:
            return "消息处理失败" + str(e)
