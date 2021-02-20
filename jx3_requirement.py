from nonebot import on_command, CommandSession
import httpx


@on_command('条件', only_to_me=False)
async def jx3_requirement(session):
    name = session.get('name', prompt='你想查询哪个奇遇的条件呢？')
    report = await check_requirement(name)
    await session.send(report)


# 命令解析器
@jx3_requirement.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['name'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询服务器名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


async def check_requirement(name):
    api = f'https://jx3api.com/api/server.php?token=153166341&server={name}'
    async with httpx.AsyncClient() as sess:
        res = await sess.get(api)
    data = res.json()
    if data == {'请求错误': '参数错误！'}:
        return '消息处理失败，请检查输入的奇遇名称是否正确！'
    else:
        msg = ("奇遇名称：{奇遇名称}\n触发方式：{触发方式}\n奇遇前置：{满足条件}\n加分项目：{其他可能}\n奇遇奖励：{物品奖励}".format(**data))
    return msg
