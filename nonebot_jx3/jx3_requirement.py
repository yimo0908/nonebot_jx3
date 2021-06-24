import httpx


async def check_requirement(name):
    api = f'https://jx3api.com/app/method?name={name}'
    async with httpx.AsyncClient() as sess:
        try:
            res = await sess.get(api)
            data = res.json()
            if data['code'] == 200:
                msg = ("奇遇名称：{name}\n触发方式：{method}\n奇遇前置：{need}\n加分项目：{other}\n奇遇奖励：{reward}".format(**data['data']))
                return msg
            else:
                return '消息处理失败，请检查输入的奇遇名称是否正确！'
        except Exception as e:
            return "消息处理失败" + str(e)
