#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

data = readJSON.j("data.json")
minren = data["famous"] # a 代表qiandian，b代表houdian
qiandian = data["before"] # 在minren前面弄点feihua
houdian = data['after']  # 在minren后面弄点feihua
feihua = data['bosh'] # 代表文章主要feihua来源

xx = "学生会退会"

chongfu = 2

def xipai(liebiao):
    global chongfu
    chi = list(liebiao) * chongfu
    while True:
        random.shuffle(chi)
        for yuansu in chi:
            yield yuansu

xiayijufeihua = xipai(feihua)
xiayijuminren = xipai(minren)

def laidianminren():
    global xiayijuminren
    xx = next(xiayijuminren)
    xx = xx.replace(  "a",random.choice(qiandian) )
    xx = xx.replace(  "b",random.choice(houdian) )
    return xx

def lingqi():
    xx = " "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    f = open('/new.txt','w')
    f.write('    ');
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 1100 ) :
            fenzhi = random.randint(0,100)
            if fenzhi < 10 and tmp[len(tmp)-2] != '\n':
                tmp += lingqi()
            elif fenzhi < 20 :
                tmp += laidianminren()
            else:
                tmp += next(xiayijufeihua)
        tmp = tmp.replace("x",xx)
        f.write(tmp)
        #print(tmp)
