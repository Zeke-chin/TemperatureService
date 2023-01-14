# TemperatureService

这个仓库包含了一个使用websockets通讯的温度服务的服务端和客户端demo代码。服务端监听来自客户端的温度更新，客户端每秒发送一次温度更新到服务端。

## 开始使用

这些说明将帮助您在本地机器上运行项目的副本，以进行开发和测试。

### 先决条件

- Python 3.7 或更高版本
- asyncio
- websockets

### 安装

将仓库克隆到本地机器：

```bash
git clone https://github.com/Zeke-chin/TemperatureService
```

### 运行服务端

要运行服务端，请导航到TemperatureService目录并运行以下命令：

```bash
python temperature_server.py
```

### 运行客户端

要运行客户端，请导航到TemperatureService目录并运行以下命令：

```bash
python temperature_client.py
```
