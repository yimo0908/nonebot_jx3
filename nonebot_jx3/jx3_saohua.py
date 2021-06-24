import httpx


async def get_saohua():
    api = 'https://jx3api.com/app/random'
    async with httpx.AsyncClient() as sess:
        try:
            res = await sess.get(api)
            dictionary = res.json()
            saohua = dictionary["data"]["text"]
            return saohua
        except Exception as e:
            return "消息处理失败" + str(e)
