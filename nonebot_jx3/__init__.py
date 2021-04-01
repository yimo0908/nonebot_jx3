from nonebot import on_command, CommandSession, scheduler, get_bot

from .jx3_CDpet import get_cdpet_pic
from .jx3_daily import get_daily_report
from .jx3_gold import get_gold_of_server
from .jx3_requirement import check_requirement
from .jx3_sand import get_sand_of_server
from .jx3_saohua import get_saohua
from .jx3_scheduledaily import scheduled_daily_report
from .jx3_server import check_server


@on_command('条件', only_to_me=False)
async def jx3_requirement(session):
    name = session.get('name', prompt='你想查询哪个奇遇的条件呢？')
    report = await check_requirement(name)
    await session.send(report)


@jx3_requirement.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['name'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询奇遇名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


@on_command('金价', only_to_me=False)
async def jx3_gold(session: CommandSession):
    user = session.event.user_id
    server = session.get('server', prompt='你想查询哪个服务器的金价呢？')
    gold_report = await get_gold_of_server(server)
    await session.send(f'[CQ:at,qq={user}]' + "\n" + gold_report)


@jx3_gold.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['server'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询服务器名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


@on_command('沙盘', only_to_me=False)
async def jx3_sand(session: CommandSession):
    user = session.event.user_id
    server = session.get('server', prompt='你想查询哪个服务器的沙盘呢？')
    report = await get_sand_of_server(server)
    await session.send(f'[CQ:at,qq={user}]' + "\n" + report)


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


@on_command('骚话', only_to_me=False)
async def jx3_sanhua(session):
    saohua = await get_saohua()
    await session.send(saohua)


@on_command('日常', only_to_me=False)
async def jx3_daily(session):
    user = session.event.user_id
    daily_report = await get_daily_report()
    await session.send(f'[CQ:at,qq={user}]' + "\n今日日常：\n" + daily_report)


@on_command('蹲宠', only_to_me=False)
async def jx3_cdpet(session):
    pic = await get_cdpet_pic()
    await session.send(pic)


@scheduler.scheduled_job('cron', hour='8')
async def jx3_scheduleddaily():
    bot = get_bot()
    msg = await scheduled_daily_report()
    await bot.send_group_msg(group_id=1003245549, message=f'今日日常：\n{msg}')
