#!/usr/bin/python3

"""
简介：
    调用apt-rdepends包查询目标软件包所需依赖，再使用apt download命令下载到当前目录
语法：
    aptdownloader <包名>
作者：
    Vladimir Yang
    0@hackerbs.com
    https://hackerbs.com
"""

import subprocess,sys

if __name__ == "__main__":
    pgName = sys.argv # 传参获取包名
    pgs = [] # 将包名存储为数组
    if len(pgName) > 1: # 忽略aptdownloader本身
        for arg in pgName[1:]:
            pgs += [arg] # 将包名依次存储
    pgs_str = ' '.join(pgs) # 使用空格分隔，将包名整理
    cmd = f'apt download $(apt-rdepends -p {pgs_str} |grep -v "^ ")' #
    # 调用apt-rdepends查询依赖并将结果传输给apt download命令
    aptInstall = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    # 执行cmd
    output = aptInstall.communicate()[0].decode("utf-8") # 使用communicate获取子进程的标准输出并格式化为utf-8编码
    print(output) # 打印执行结果
