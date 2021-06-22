import httpx


async def get_gold_of_server(server: str) -> str:
    api = f'https://jx3api.com/app/gold?server={server}'
    async with httpx.AsyncClient() as sess:
        res = await sess.get(api)
    dictionary = res.json()
    if dictionary['code'] == 400:
        return '消息处理失败，请检查输入的服务器名称是否正确！'
    else:
        d = dictionary["data"]
        send_msg = "%s的金价：\n万宝楼：%s\nuu898：%s\ndd373：%s\n5173：%s\n7881：%s" % (
            d['server'], d['wanbaolou'], d['uu898'], d['dd373'], d['5173'], d['7881'])
    return send_msg
