import httpx


async def get_sand_of_server(server):
    api = 'https://jx3api.com/app/sand?server={}'.format(server)
    async with httpx.AsyncClient() as sess:
        try:
            res = await sess.get(api)
            dictionary = res.json()
            if dictionary['code'] == 200:
                image_url = dictionary["data"]["url"]
                return f'[CQ:image,file={image_url},cache=0]'
            else:
                return '消息处理失败，请检查输入的服务器名称是否正确！'
        except Exception as e:
            return "消息处理失败" + str(e)
