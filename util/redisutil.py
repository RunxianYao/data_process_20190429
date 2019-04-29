# -*- coding: utf-8 -*-

import redis
import configparser
import os

# 获取当前路径
curr_dir = os.path.dirname(os.path.realpath(__file__))
# 完整路径redis
redis_conf = curr_dir + os.sep + "redis.conf"

Config = configparser.ConfigParser()
Config.read(redis_conf)
print "路径" + redis_conf
RedisResource = redis.Redis(host=Config.get("redis", "host"),port=Config.get("redis", "port"),
                            password=Config.get("redis", "password"))







