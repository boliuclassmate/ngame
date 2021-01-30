# -*- coding: UTF-8 -*-
from runner.extapi import *
# 添加用户封装
# from userlib.demo_lib import *
# TODO: write your code


def kai_shi(*args, **kwargs):
    """
        开始
    """
    #TODO: 这里编写具体代码
    try:
        # 隐私协议
        click('obj_1610959532948.jpg', position=(0.524, 0.737, 0.637, 0.82), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('同意')
    sleep(8)

    try:
        # 权限列表
        if exists('obj_1610959609727.jpg', timeOut=20, by=DriverType.CV):
            click('obj_1610959636892.jpg', position=(0.449, 0.774, 0.548, 0.858), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        logger.info('权限同意')
    sleep(4)

    while True:
        # 循环更新
        if exists('obj_1610961409484.jpg', timeOut=20, by=DriverType.CV):
            click('obj_1610961409484.jpg', position=(0.508, 0.721, 0.651, 0.796), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
            break
        else:
            click((0.48, 0.157), position=None)
            if exists('obj_1610961334505.jpg', timeOut=20, by=DriverType.CV):
                click('obj_1610961348571.jpg', position=(0.916, 0.031, 0.944, 0.102), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
                sleep(4)
    sleep(24)


def denglu(*args, **kwargs):

    try:
        playWithQQFriends(locator = 'obj_1610961470964.jpg', acc = '', pwd = '', timeOut = 240)
    except:
        logger.info('QQ登录')
    sleep(8)


    try:
        # 开始游戏
        click('obj_1610961559451.jpg', position=(0.406, 0.731, 0.587, 0.827), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('开始游戏')
    sleep(8)

    if exists('obj_1611044050202.jpg', timeOut=20, by=DriverType.CV):
        click('obj_1611044050202.jpg', position=(0.429, 0.762, 0.568, 0.827), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    sleep(30)


def dating(*args, **kwargs):
    """
        大厅
    """
    #TODO: 这里编写具体代码
    try:
        # 活动 
        click('obj_1610961813461.jpg', position=(0.918, 0.303, 0.948, 0.381), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        logger.info('图片文字点击活动')
    except:
        try:
            click('obj_1610963253570.jpg', xOffset=-0.046,yOffset=-0.002, position=(0.914, 0.3, 0.95, 0.384))
            logger.info('偏移点击活动')
        except:
            click((0.932, 0.334), position=None)
            logger.info('坐标点击活动')
    sleep(6)

    try:
        if not exists('obj_1611026423169.jpg', timeOut=20, by=DriverType.CV):  
            # slide('obj_1611043680362.jpg','obj_1611043495445.jpg')
            slide((0.188, 0.738), (0.192, 0.502))
    except:
        pass
    sleep(3)
    
    try:
        # 千年长安
        click('obj_1611026423169.jpg', position=(0.137, 0.638, 0.202, 0.724), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        try:
            click_text('千年长安')
            logger.info('文字点击')
        except:
            click('obj_1611026477102.jpg', xOffset=0.074,yOffset=0, position=(0.054, 0.619, 0.113, 0.731))
            logger.info('千年长安偏移点击')
    sleep(4)

    try:
        # 获取卡牌
        click('obj_1611026902237.jpg', position=(0.629, 0.851, 0.711, 0.907), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('获取卡牌')
    sleep(4)

    try:    
        # 一键召集
        click('obj_1611026943988.jpg', position=(0.535, 0.811, 0.657, 0.879), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('一键召集')
    sleep(8)


    try:
        # 卡牌赠予分享
        click('obj_1611027523911.jpg', position=(0.252, 0.155, 0.339, 0.433), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.294, 0.308), position=None)
    sleep(6)

    try:
        # 关闭分享牌
        click('obj_1611028099275.jpg', position=(0.654, 0.118, 0.691, 0.198), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.671, 0.154), position=None)
    sleep(4)

    try:
        # 关闭获取卡牌
        click('obj_1611028587080.jpg', position=(0.784, 0.09, 0.813, 0.152), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.795, 0.121), position=None)
    sleep(6)


    try:
        # 活动规则
        click('obj_1611027270842.jpg', position=(0.767, 0.477, 0.787, 0.52), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.776, 0.495), position=None)
    sleep(8)

    try:
        # 关闭活动规则
        click('obj_1611027321633.jpg', position=(0.692, 0.204, 0.721, 0.279), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click((0.705, 0.243), position=None)
    sleep(4)


    try:
        # 活动页签切换2
        click('obj_1611026568430.jpg', position=(0.764, 0.7, 0.856, 0.759), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('曲池坊')
    sleep(8)

    try:
        # 活动页签切换3
        click('obj_1611026641762.jpg', position=(0.768, 0.783, 0.851, 0.854), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('郢酒坊')
    sleep(8)