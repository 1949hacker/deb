[English](./README_en.md)

[官网地址:https://hackerbs.com/](https://hackerbs.com/)

# 使用说明

建议通过添加源的方式安装`aptdownloader`

```shell
wget -O - https://apt.ygeit.cn/public.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/ygeit.gpg
echo "deb [signed-by=/etc/apt/trusted.gpg.d/ygeit.gpg] https://apt.ygeit.cn bookworm main" >> /etc/apt/sources.list
apt update
```

`aptdownloader <package name>`

该命令会下载指定的包及其依赖到当前目录中，多个包名用空格分隔，示例：

`aptdownloader docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

**注意事项：该工具下载的包及其依赖是基于当前系统的，所以你要离线导入deb包的目标系统也必须是相同系统才可！**

# 工具原理

原命令`apt download $(apt-rdepends -p <package name> | grep -v "^ ")`

使用python sys传参，subprocess执行命令，简化了原命令的操作方式
