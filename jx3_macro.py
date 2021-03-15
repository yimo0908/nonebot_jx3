import httpx
from nonebot import on_command


@on_command('冰心宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=冰心诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('气纯宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=紫霞功'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('剑纯宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=太虚剑意'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('花间宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=花间游'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('易筋宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=易筋经'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('洗髓宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=洗髓经'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('傲血宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=傲血战意'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('铁牢宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=铁牢律'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('藏剑宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=问水诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('毒经宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=毒经'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('惊羽宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=惊羽诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('天罗宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=天罗诡道'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('丐帮宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=笑尘诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('分山宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=分山劲'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('铁骨宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=铁骨衣'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('焚影宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=焚影圣诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('明尊宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=明尊琉璃体'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('莫问宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=莫问'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('霸刀宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=北傲诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('蓬莱宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=凌海诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('凌雪宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=隐龙诀'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)


@on_command('衍天宏', only_to_me=False)
async def jx3_macro(session):
    api = f'https://jx3api.com/app/getMacro?name=太玄经'
    res = httpx.get(api)
    macro = res.text
    await session.send(macro)
