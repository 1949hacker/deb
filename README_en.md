[HomePage:https://hackerbs.com/](https://hackerbs.com/)

# User Guide

Recommend installing `aptdownloader` via the APT source.

```shell
wget -O - https://apt.ygeit.cn/public.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/ygeit.gpg
echo "deb [signed-by=/etc/apt/trusted.gpg.d/ygeit.gpg] https://apt.ygeit.cn bookworm main" >> /etc/apt/sources.list
apt update
```

`aptdownloader <package name>`

This command downloads the specified package and its dependencies to the current directory. Multiple package names should be separated by spaces. For example:

`aptdownloader docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

**Note: The packages and their dependencies downloaded by this tool are based on the current system. Therefore, the target system for offline package import must be the same as the current system!**

# Tool Principle

The original command is:`apt download $(apt-rdepends -p <package name> | grep -v "^ ")`

The tool uses Python's sys for parameter passing and subprocess for command execution, simplifying the operation of the original command.
