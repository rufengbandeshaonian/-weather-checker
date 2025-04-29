# Weather Checker

一个简单的 Python 项目，用于通过天气 API 获取城市当前天气。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方式

```python
from weather.checker import get_weather

print(get_weather("Beijing", "your_api_key"))
```
# Weather Checker

一个简单的 Python 项目，用于通过 WeatherAPI 获取城市当前天气信息。

---

## 一、安装步骤

1. 克隆或下载本项目，然后进入目录：

```bash
cd weather-checker
```

2. （可选）创建并激活虚拟环境：

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

---

## 二、获取 WeatherAPI 的 API Key

1. 前往：https://www.weatherapi.com/
2. 注册账号并获取你的免费 API Key
3. 记下它，用于后续查询天气

---

## 三、运行项目示例

你可以创建一个脚本 `run.py`，内容如下：

```python
from weather.checker import get_weather

if __name__ == "__main__":
    city = input("请输入城市名：")
    api_key = "你的API_KEY"
    weather = get_weather(city, api_key)
    print(weather)
```

然后在终端运行：

```bash
python run.py
```

---

## 四、运行测试（可选）

项目内置了简单的单元测试，可用以下命令运行：

```bash
python -m unittest discover tests
```

---

## 项目结构说明

```
weather-checker/
├── weather/              # 核心功能模块
│   ├── __init__.py
│   └── checker.py        # 天气获取函数
├── tests/                # 测试模块
│   └── test_checker.py
├── requirements.txt      # 所需依赖
├── README.md             # 项目说明
├── setup.py              # 安装配置
└── .gitignore
```

---
