from nonebot import on_command, CommandSession
import httpx
import json


@on_command('开服', only_to_me=False)
async def jx3_server(session):
    user = session.event.user_id
    server = session.get('server', prompt='你想查询哪个服务器的状态呢？')
    report = await check_server(server, user)
    await session.send(report)


# 命令解析器
@jx3_server.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['server'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询服务器名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


async def check_server(server, user):
    api = f'https://jx3api.com/next/server.php?token=jx3zhenhaowan&server={server}'
    async with httpx.AsyncClient() as sess:
        res = sess.get(api)
    dictionary = res.json()
    if dictionary['code'] == 0:
        return '消息处理失败，请检查输入的服务器名称是否正确！'
    if dictionary["data"]["status"] == 1:
        msg = f'[CQ:at,qq={user}]' + dictionary["data"]["server"] + "已开服"
    else:
        msg = f'[CQ:at,qq={user}]' + dictionary["data"]["server"] + "未开服"
    return msg
