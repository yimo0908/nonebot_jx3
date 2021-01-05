from nonebot import on_command, CommandSession
import httpx
import json


@on_command('沙盘', only_to_me=False)
async def jx3_sand(session: CommandSession):
    user = session.event.user_id
    server = session.get('server', prompt='你想查询哪个服务器的沙盘呢？')
    report = await get_sand_of_server(server)
    await session.send(f'[CQ:at,qq={user}]' + "\n" + report)


# 命令解析器
@jx3_sand.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['server'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询服务器名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


async def get_sand_of_server(server):
    api = 'https://jx3api.com/api/sand.php?token=jx3zhenhaowan&server={}'.format(server)
    async with httpx.AsyncClient() as sess:
        try:
            res = await sess.get(api)
        except Exception as e:
            return str(e)
    dictionary = res.json()
    if dictionary['code'] == 0:
        return '消息处理失败，请检查输入的服务器名称是否正确！'
    image_url = dictionary["data"]["url"]
    return f'[CQ:image,file={image_url},cache=0]'
