from nonebot import on_command, CommandSession
import httpx


@on_command('金价', only_to_me=False)
async def jx3_gold(session: CommandSession):
    user = session.event.user_id
    # 从会话状态（session.state）中获取服务器名称（server），如果当前不存在，则询问用户
    server = session.get('server', prompt='你想查询哪个服务器的金价呢？')
    gold_report = await get_gold_of_server(server)
    # 向用户发送金价
    await session.send(f'[CQ:at,qq={user}]' + "\n" + gold_report)


# 命令解析器
@jx3_gold.args_parser
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


async def get_gold_of_server(server: str) -> str:
    api = f'https://nico.nicemoe.cn/app/getGold?server={server}'
    async with httpx.AsyncClient() as sess:
        res = await sess.get(api)
    dictionary = res.json()
    if dictionary['code'] == 400:
        return '消息处理失败，请检查输入的服务器名称是否正确！'
    send_msg =("{server}的金价：\n万宝楼：{wanbaolou}\n游募：{youmu}\nuu898：{uu898}\ndd373：{dd373}\n5173：{5173}\n7881：{7781}".format(**dictionary["data"]))
    return send_msg
