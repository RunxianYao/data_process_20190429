# -*- coding: utf-8 -*-

# KEy 生成工具
number = 'PHONE_NUMBER';
imsi = 'IMSI';
rg_info = 'REGISTER_INFO';
colon = ':';
tophonenumber = 'TOPHONENUMBER';

# PHONE_NUMBER:${phoneNumber}:IMSI:${imsi}:REGISTER_INFO
def phonenumber_imsi_register_info(phonenumber,imsi):
    return number + colon +phonenumber+ colon + imsi + colon + rg_info

# IMSI:${imsi}:TOPHONENUMBER
def imsi_tophonenumber(imsi):
    return imsi + colon + imsi + colon + tophonenumber


# PHONE_NUMBER:${phoneNumber}:REGISTER_INFO
def phonenumber_rg_info(phonenumber):
    return  number + colon + phonenumber + colon + rg_info

