import httpx


async def get_saohua():
    api = 'https://jx3api.com/app/getRandom'
    async with httpx.AsyncClient() as sess:
        try:
            res = await sess.get(api)
        except Exception as e:
            return str(e)
    dictionary = res.json()
    if dictionary['code'] == 0:
        return '消息处理失败，请检查输入的服务器名称是否正确！'
    saohua = dictionary["data"]["text"]
    return saohua
