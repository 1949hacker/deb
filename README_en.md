[HomePage:https://1949hacker.cn/](https://1949hacker.cn/)

# User Guide

Recommend installing `aptdownloader` via the APT source.

```shell
echo "deb [trusted=yes] http://apt.1949hacker.cn:20888 ./" >> /etc/apt/sources.list
apt update
```

`aptdownloader <package name>`

This command downloads the specified package and its dependencies to the current directory. Multiple package names should be separated by spaces. For example:

`aptdownloader docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

**Note: The packages and their dependencies downloaded by this tool are based on the current system. Therefore, the target system for offline package import must be the same as the current system!**

# Tool Principle

The original command is:`apt download $(apt-rdepends -p <package name> | grep -v "^ ")`

The tool uses Python's sys for parameter passing and subprocess for command execution, simplifying the operation of the original command.