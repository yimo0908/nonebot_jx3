from nonebot import on_command, CommandSession
import httpx
import json


@on_command('开服', only_to_me=False)
async def jx3_server(session):
    user = session.event.user_id
    server = session.get('server', prompt='你想查询哪个服务器的状态呢？')
    report = await check_server(server, user)
    # 向用户发送金价
    await session.send(report)


# 命令解析器
@jx3_server.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将服务器名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：金价 绝代
            session.state['server'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询服务器名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的服务器），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def check_server(server, user):
    api = f'https://jx3api.com/next/server.php?token=jx3zhenhaowan&server={server}'
    res = httpx.get(api)
    dictionary = json.loads(res.content)
    if dictionary["data"]["status"] == 1:
        msg = f'[CQ:at,qq={user}]' + dictionary["data"]["server"] + "已开服"
    else:
        msg = f'[CQ:at,qq={user}]' + dictionary["data"]["server"] + "未开服"
    return msg
