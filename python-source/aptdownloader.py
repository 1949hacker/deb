#!/usr/bin/python3

"""
简介：
    调用apt-rdepends包查询目标软件包所需依赖，再使用apt download命令下载到当前目录
语法：
    aptdownloader <包名>
作者：
    Vladimir Yang
    scepter@1949hacker.cn
    https://1949hacker.cn
"""

import subprocess,sys

if __name__ == "__main__":
    pgName = sys.argv
    pgs = []
    if len(pgName) > 1:
        for arg in pgName[1:]:
            print(arg)
    cmd = ["apt",
           "download",
           "$(apt-rdepends\0-p",
           pgs,
           "|",
           "grep",
           "-v",
           "\"^",
           "\")"]
    aptInstall = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
    output = aptInstall.communicate()[0].decode("utf-8")
    print(output)
