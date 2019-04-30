# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from util.redisutil import RedisResource
import util.KeyUtil as KeyUtil
import logging
from logging import handlers
import string

class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    } # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)

# 表数据处理
def add_table_and_rename():
    # 获取日志记录器
    log = Logger("process_log",level='info')
    log.logger.info("开始处理生成IMSI表，及重命名原表")
    # PHONE_NUMBER:${phoneNumber}:IMSI:${imsi}:REGISTER_INFO
    phonenumber_imsi_reg_info = KeyUtil.phonenumber_imsi_register_info("*","*")
    allKeys = RedisResource.keys(phonenumber_imsi_reg_info)
    for key in allKeys :
        print("满足条件的KEY：" + key)
        msg = "满足条件的KEY：" + key
        log.logger.info(msg)
        # 生成新的表
        keyarr = string.split(key,KeyUtil.colon)
        print(keyarr)
        imsi = keyarr[3]
        phone_number = keyarr[1]
        #新增表
        table_name = KeyUtil.imsi_tophonenumber(imsi)
        log.logger.info("ADD_NEW_TABLE[%s]",table_name)
        RedisResource.set(table_name,phone_number)

        #修改原来表名
        new_table = KeyUtil.phonenumber_rg_info(phone_number)
        log.logger.info("OLD_TABLE[%s]->NEW_TABLE[%s]",key,new_table)
        # RedisResource.rename(key,new_table)
    log.logger.info("流程处理完毕，程序退出！！")



