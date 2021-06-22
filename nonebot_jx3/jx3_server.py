from nonebot import on_command, CommandSession
import httpx


async def check_server(server, user):
    api = f'https://jx3api.com/app/check?server={server}'
    async with httpx.AsyncClient() as sess:
        res = await sess.get(api)
    dictionary = res.json()
    if dictionary['code'] == 400:
        return '消息处理失败，请检查输入的服务器名称是否正确！'
    if dictionary["data"]["status"] == 1:
        msg = f'[CQ:at,qq={user}]' + dictionary["data"]["region"] + dictionary["data"]["server"] + "已开服"
    else:
        msg = f'[CQ:at,qq={user}]' + dictionary["data"]["region"] + dictionary["data"]["server"] + "未开服"
    return msg
