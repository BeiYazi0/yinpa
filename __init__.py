import hoshino
from hoshino import Service, util, priv
from hoshino.typing import CQEvent, MessageSegment

import asyncio
import random
import time
from random import choice
from typing import Tuple

from .txt2img import txt_to_img
from .utils import utils


sv = Service(
    name="impact",  # 功能名
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle="娱乐",  # 分组归类
    help_="发送【淫趴介绍|银趴介绍】了解更多",  # 帮助说明

)


@sv.on_prefix(("pk", "对决"))
async def pk(bot, event: CQEvent) -> None:
    """pk的响应器"""
    if not (await utils.check_group_allow(str(event.group_id))):
        await bot.finish(event, utils.not_allow, at_sender=True)
    uid: str = str(event.user_id)
    allow: bool = await utils.pkcd_check(uid)     # CD是否允许pk
    if not allow:       # 如果不允许pk, 则返回
        await bot.finish(event, f"你已经pk不动了喵, 请等待{round(utils.pk_cd_time-(time.time() - utils.pk_cd_data[uid]),3)}秒后再pk喵", at_sender=True)
    utils.pk_cd_data.update({uid: time.time()})    # 更新CD时间
    at = await utils.get_at(event)            # 获取at的id, 类型为str
    if at == "寄":
        await bot.finish(event, "请at你要pk的对象哦", at_sender=True)
    if at == uid:   # 如果at的id和uid相同, 则返回
        await bot.finish(event, "你不能pk自己喵", at_sender=True)
    if uid in utils.userdata and at in utils.userdata:  # 如果两个都在userdata里面
        random_num = random.random()    # 生成一个随机数
        # 如果random_num大于0.5, 则胜利, 否则失败
        if random_num > 0.5:
            random_num: float = utils.get_random_num()  # 重新生成一个随机数
            utils.userdata.update(
                {uid: round(utils.userdata[uid] + (random_num/2), 3)})  # 更新userdata
            # 更新userdata
            utils.userdata.update({at: round(utils.userdata[at] - random_num, 3)})
            utils.write_user_data()    # 写入文件
            await bot.finish(event, f"对决胜利喵, 你的{choice(utils.jj_variable)}增加了{round(random_num/2,3)}cm喵, 对面则在你的阴影笼罩下减小了{random_num}cm喵", at_sender=True)
        else:
            random_num: float = utils.get_random_num()    # 重新生成一个随机数
            utils.userdata.update(
                {uid: round(utils.userdata[uid] - random_num, 3)})  # 更新userdata
            # 更新userdata
            utils.userdata.update({at: round(utils.userdata[at] + random_num/2, 3)})
            utils.write_user_data()    # 写入文件
            await bot.finish(event, f"对决失败喵, 在对面牛子的阴影笼罩下你的{choice(utils.jj_variable)}减小了{random_num}cm喵, 对面增加了{round(random_num/2,3)}cm喵", at_sender=True)
    else:
        # 谁不在userdata里面, 就创建谁
        if uid not in utils.userdata:
            utils.userdata.update({uid: 10})   # 创建用户
        if at not in utils.userdata:
            utils.userdata.update({at: 10})    # 创建用户
        utils.write_user_data()     # 写入文件
        del utils.pk_cd_data[uid]   # 删除CD时间
        await bot.send(event, f"你或对面还没有创建{choice(utils.jj_variable)}喵, 咱全帮你创建了喵, 你们的{choice(utils.jj_variable)}长度都是10cm喵", at_sender=True)


@sv.on_rex("^(打胶|开导)$")
async def dajiao(bot, event: CQEvent) -> None:
    """打胶的响应器"""
    if not (await utils.check_group_allow(str(event.group_id))):
        await bot.finish(event, utils.not_allow, at_sender=True)
    uid: str = str(event.user_id)
    allow = await utils.cd_check(uid)    # CD是否允许打胶
    if not allow:   # 如果不允许打胶, 则返回
        await bot.finish(event, f"你已经打不动了喵, 请等待{round(utils.dj_cd_time-(time.time() - utils.cd_data[uid]),3)}秒后再打喵", at_sender=True)
    utils.cd_data.update({uid: time.time()})    # 更新CD时间
    if uid in utils.userdata:    # 如果在userdata里面
        random_num = utils.get_random_num()    # 生成一个随机数
        utils.userdata.update(
            {uid: round(utils.userdata[uid] + random_num, 3)})  # 更新userdata
        utils.write_user_data()    # 写入文件
        await bot.finish(event, f"打胶结束喵, 你的{choice(utils.jj_variable)}很满意喵, 长了{random_num}cm喵, 目前长度为{utils.userdata[uid]}cm喵", at_sender=True)
    else:
        utils.userdata.update({uid: 10})   # 创建用户
        utils.write_user_data()    # 写入文件
        del utils.cd_data[uid]     # 删除CD时间
        await bot.send(event, f"你还没有创建{choice(utils.jj_variable)}, 咱帮你创建了喵, 目前长度是10cm喵", at_sender=True)

                
@sv.on_prefix("嗦牛子")
async def suo(bot, event: CQEvent) -> None:
    """嗦牛子的响应器"""
    if not (await utils.check_group_allow(str(event.group_id))):
        await bot.finish(event, utils.not_allow, at_sender=True)
    uid: str = str(event.user_id)
    allow = await utils.suo_cd_check(uid)   # CD是否允许嗦
    if not allow:   # 如果不允许嗦, 则返回
        await bot.finish(event, f"你已经嗦不动了喵, 请等待{round(utils.suo_cd_time-(time.time() - utils.suo_cd_data[uid]),3)}秒后再嗦喵", at_sender=True)
    utils.suo_cd_data.update({uid: time.time()})    # 更新CD时间
    at: str = await utils.get_at(event)    # 获取at的用户id, 类型为str
    if at == "寄":  # 如果没有at
        if uid in utils.userdata:   # 如果在userdata里面
            random_num = utils.get_random_num()    # 生成一个随机数
            utils.userdata.update(
                {uid: round(utils.userdata[uid] + random_num, 3)})  # 更新userdata
            utils.write_user_data()    # 写入文件
            await bot.finish(event, f"你的{choice(utils.jj_variable)}很满意喵, 嗦长了{random_num}cm喵, 目前长度为{utils.userdata[uid]}cm喵", at_sender=True)
        else:   # 如果不在userdata里面
            utils.userdata.update({uid: 10})   # 创建用户
            utils.write_user_data()    # 写入文件
            del utils.suo_cd_data[uid]     # 删除CD时间
            await bot.finish(event, f"你还没有创建{choice(utils.jj_variable)}喵, 咱帮你创建了喵, 目前长度是10cm喵", at_sender=True)
    elif at in utils.userdata:  # 如果在userdata里面
        random_num = utils.get_random_num()    # 生成一个随机数
        # 更新userdata
        utils.userdata.update({at: round(utils.userdata[at] + random_num, 3)})
        utils.write_user_data()    # 写入文件
        await bot.finish(event, f"对方的{choice(utils.jj_variable)}很满意喵, 嗦长了{random_num}cm喵, 目前长度为{utils.userdata[at]}cm喵", at_sender=True)
    else:
        utils.userdata.update({at: 10})    # 创建用户
        utils.write_user_data()    # 写入文件
        del utils.suo_cd_data[uid]     # 删除CD时间
        await bot.send(event, f"他还没有创建{choice(utils.jj_variable)}喵, 咱帮他创建了喵, 目前长度是10cm喵", at_sender=True)


@sv.on_prefix("查询jj")
async def queryjj(bot, event: CQEvent) -> None:
    """查询某人jj的响应器"""
    if not (await utils.check_group_allow(str(event.group_id))):
        await bot.finish(event, utils.not_allow, at_sender=True)
    uid: str = str(event.user_id)   # 获取用户id, 类型为str
    at: str = await utils.get_at(event)    # 获取at的用户id, 类型为str
    if at == "寄":  # 如果没有at
        if uid in utils.userdata:  # 如果在userdata里面
            await bot.finish(event, f"你的{choice(utils.jj_variable)}目前长度为{utils.userdata[uid]}cm喵", at_sender=True)
        else:
            utils.userdata.update({uid: 10})   # 创建用户
            utils.write_user_data()    # 写入文件
            await bot.finish(event, f"你还没有创建{choice(utils.jj_variable)}喵, 咱帮你创建了喵, 目前长度是10cm喵", at_sender=True)
    elif at in utils.userdata:  # 如果在userdata里面
        await bot.finish(event, f"他的{choice(utils.jj_variable)}目前长度为{utils.userdata[at]}cm喵", at_sender=True)
    else:
        utils.userdata.update({at: 10})    # 创建用户
        utils.write_user_data()    # 写入文件
        await bot.finish(event, f"他还没有创建{choice(utils.jj_variable)}喵, 咱帮他创建了喵, 目前长度是10cm喵", at_sender=True)


@sv.on_fullmatch(("jj排行榜", "jj排名", "jj榜单", "jjrank"))
async def jjrank(bot, event: CQEvent) -> None:
    """输出前五后五和自己的排名"""
    if not (await utils.check_group_allow(str(event.group_id))):
        await bot.finish(event, utils.not_allow, at_sender=True)
    uid: str = str(event.user_id)
    rankdata: list = sorted(utils.userdata.items(),
                    key=lambda x: x[1], reverse=True)   # 排序
    if len(rankdata) < 5:
        await bot.finish(event, "目前记录的数据量小于5, 无法显示rank喵")
    top5: list = rankdata[:5]    # 取前5
    last5: list = rankdata[-5:]   # 取后5
    index = [i for i, x in enumerate(rankdata) if x[0] == uid]  # 获取用户排名
    if not index:   # 如果用户没有创建JJ
        utils.userdata.update({uid: 10})   # 创建用户
        utils.write_user_data()    # 写入文件
        await bot.finish(event, f"你还没有创建{choice(utils.jj_variable)}看不到rank喵, 咱帮你创建了喵, 目前长度是10cm喵", at_sender=True)
    # top5和end5的信息，然后获取其网名
    top5info = [await bot.get_stranger_info(user_id=int(name[0])) for name in top5]
    last5info = [await bot.get_stranger_info(user_id=int(name[0])) for name in last5]
    top5names = [name["nickname"] for name in top5info]
    last5names = [name["nickname"] for name in last5info]
    # 构造消息，手搓
    reply = "咱只展示前五名和后五名喵\n"
    top5txt = f"{top5names[0]} ------> {top5[0][1]}cm\n{top5names[1]} ------> {top5[1][1]}cm\n{top5names[2]} ------> {top5[2][1]}cm\n{top5names[3]} ------> {top5[3][1]}cm\n{top5names[4]} ------> {top5[4][1]}cm\n"
    last5txt = f"{last5names[0]} ------> {last5[0][1]}cm\n{last5names[1]} ------> {last5[1][1]}cm\n{last5names[2]} ------> {last5[2][1]}cm\n{last5names[3]} ------> {last5[3][1]}cm\n{last5names[4]} ------> {last5[4][1]}cm\n"
    img_bytes = await txt_to_img.txt_to_img(
        top5txt+".................................\n"*3+last5txt)    # 生成图片
    reply2 = f"你的排名为{index[0]+1}喵"
    await bot.send(event, reply+MessageSegment.image(img_bytes)+reply2, at_sender=True)


async def yinpa_prehandle(bot, event: CQEvent) -> Tuple[int, int, str, str, list]:
    """透群员的预处理环节"""
    gid, uid  = event.group_id, event.user_id
    if not (await utils.check_group_allow(str(gid))):
        await bot.finish(event, utils.not_allow, at_sender=True)
    allow = await utils.fuck_cd_check(event)  # CD检查是否允许
    if not allow:
        await bot.finish(event, f"你已经榨不出来任何东西了, 请先休息{round(utils.fuck_cd_time-(time.time() - utils.ejaculation_cd[str(uid)]),3)}秒", at_sender=True)
    utils.ejaculation_cd.update({str(uid): time.time()})  # 记录时间
    req_user_card = await utils.get_user_card(bot, group_id=int(gid), qid=int(uid))
    prep_list = await bot.get_group_member_list(group_id=gid)
    return gid,uid,req_user_card, event.message.extract_plain_text(), prep_list
    

async def yinpa_member_handle(prep_list: list, req_user_card: str, bot, event: CQEvent) -> str:
    prep_list = [prep.get("user_id", 114514) for prep in prep_list]  # 群友列表
    target = await utils.get_at(event)    # 获取消息有没有at
    if target == "寄":              # 没有的话
        # 随机抽取幸运成员
        prep_list.remove(event.user_id)
        lucky_user = choice(prep_list)
        await bot.send(event, f"现在咱将随机抽取一位幸运裙友\n送给{req_user_card}色色！")
    else:                           # 有的话lucky user就是at的人
        lucky_user = target
    return str(lucky_user)
    
async def yinpa_owner_handle(uid: int, prep_list: list, req_user_card: str, bot, event: CQEvent) -> str:
    lucky_user: str = next(
        (prep['user_id'] for prep in prep_list if prep['role'] == 'owner'),
        str(uid),
    )
    if int(lucky_user) == uid:      # 如果群主是自己
        del utils.ejaculation_cd[str(uid)]
        await bot.finish(event, "你透你自己?")
    await bot.send(event, f"现在咱将把群主\n送给{req_user_card}色色！")
    return str(lucky_user)


async def yinpa_admin_handle(uid: int, prep_list: list, req_user_card: str, bot, event: CQEvent) -> str:
    admin_id: list = [prep['user_id'] for prep in prep_list if prep['role'] == 'admin']
    if uid in admin_id:         # 如果自己是管理的话， 移除自己
        admin_id.remove(uid)
    if not admin_id:          # 如果没有管理的话, del cd信息， 然后finish
        del utils.ejaculation_cd[str(uid)]
        await bot.finish(event, "喵喵喵? 找不到群管理!")
    lucky_user: str = choice(admin_id)   # random抽取一个管理
    await bot.send(event, f"现在咱将随机抽取一位幸运管理\n送给{req_user_card}色色！")
    return str(lucky_user)

async def yinpa_identity_handle(command: str, prep_list: list, req_user_card: str, bot, event: CQEvent) -> str:
    uid: int = event.user_id
    if "群主" in command:  # 如果发送的命令里面含有群主， 说明在透群主
        return await yinpa_owner_handle(uid, prep_list, req_user_card, bot, event)
    elif "管理" in command:  # 如果发送的命令里面含有管理， 说明在透管理
        return await yinpa_admin_handle(uid, prep_list, req_user_card, bot, event)
    else:       # 最后是群员
        return await yinpa_member_handle(prep_list, req_user_card, bot, event)
    

@sv.on_rex(r"^(日群友|透群友|日群主|透群主|日管理|透管理)")
async def yinpa(bot, event: CQEvent) -> None:
    gid, uid, req_user_card, command ,prep_list= await yinpa_prehandle(bot=bot, event=event)
    lucky_user: str = await yinpa_identity_handle(command=command, prep_list=prep_list, req_user_card=req_user_card, bot=bot, event=event)
    # 获取群名片或者网名
    lucky_user_card = await utils.get_user_card(bot, gid, int(lucky_user))
    # 1--100的随机数， 保留三位
    ejaculation = round(random.uniform(1, 100), 3)
    try:
        temp = (
            utils.ejaculation_data[lucky_user][utils.get_today()][
                "ejaculation"
            ]
            + ejaculation
        )
        await utils.update_ejaculation(round(temp, 3), lucky_user)
    except Exception:
        await utils.update_ejaculation(ejaculation, lucky_user)
    await asyncio.sleep(2)  # 休眠2秒, 更有效果
    # 准备调用api, 用来获取头像
    repo_1 = f"好欸！{req_user_card}({uid})用时{random.randint(1, 20)}秒 \n给 {lucky_user_card}({lucky_user}) 注入了{ejaculation}毫升的脱氧核糖核酸, 当日总注入量为：{utils.get_today_ejaculation(lucky_user)}"
    image = f"[CQ:image,file=http://q1.qlogo.cn/g?b=qq&nk={lucky_user}&s=640]"
    await bot.send(event, repo_1 + image)  # 结束


@sv.on_rex(r"^(开始银趴|关闭银趴|开启淫趴|禁止淫趴|开启银趴|禁止银趴)")
async def open_module(bot, event: CQEvent) -> None:
    """开关"""
    if not priv.check_priv(event, priv.ADMIN):
       await bot.finish(ev, '只有群管理才能开启或禁止银趴哦。', at_sender=True)
       return
    gid = str(event.group_id)
    command: str = event.message.extract_plain_text()
    if "开启" in command or "开始" in command:
        if gid in utils.groupdata:
            utils.groupdata[gid]["allow"] = True
        else:
            utils.groupdata.update({gid: {"allow": True}})
        utils.write_group_data()
        await bot.send(event, "功能已开启喵")
    elif "禁止" in command or "关闭" in command:
        if gid in utils.groupdata:
            utils.groupdata[gid]["allow"] = False
        else:
            utils.groupdata.update({gid: {"allow": False}})
        utils.write_group_data()
        await bot.send(event, "功能已禁用喵")


@sv.on_prefix(("注入查询", "摄入查询", "射入查询"))
async def query_injection(bot, event: CQEvent) -> None:
    """查询某人的注入量"""
    if not (await utils.check_group_allow(str(event.group_id))):
        await bot.finish(event, utils.not_allow, at_sender=True)
    target = event.message.extract_plain_text()  # 获取命令参数
    user_id: str = str(event.user_id)
    # 判断带不带at
    [object_id, replay1] = [await utils.get_at(event), "该用户"] if await utils.get_at(event) != "寄" else [user_id, "您"]
    ejaculation = 0             # 先初始化0
    if "历史" in target or "全部" in target:
        try:
            date = utils.ejaculation_data[object_id]  # 对象不存在直接输出0
        except Exception:
            await bot.finish(event, f"{replay1}历史总被注射量为0ml")
        pic_string: str = ""            # 文字， 准备弄成图片
        for key in date:                # 遍历所有的日期
            temp = date[key]["ejaculation"]
            ejaculation += temp             # 注入量求和
            pic_string += f"{key}\t\t{temp}\n"
            
        await bot.send(event, MessageSegment.text(f"{replay1}历史总被注射量为{ejaculation}ml")+MessageSegment.image(await txt_to_img.txt_to_img(pic_string)))
    else:
        ejaculation = utils.get_today_ejaculation(object_id)  # 获取对象当天的注入量
        await bot.send(event, f"{replay1}当日总被注射量为{ejaculation}ml")


@sv.on_fullmatch(("淫趴介绍", "银趴介绍"))
async def yinpa_introduce(bot, event: CQEvent) -> None:
    """输出用法"""
    await bot.send(event, MessageSegment.image(await utils.plugin_usage()))

