# 周大仙：你的赛博算命大师
**该项目参考[narrator: David Attenborough narrates your life](https://github.com/cbh123/narrator)，感谢原开发者的贡献。**

![](assets/bagua.jpg)

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README_CN.md">简体中文</a> |
</p>

## 想要知道你今日运势？让周大仙来给你看看:>

今天会不会在路上捡到钱？会不会被老板猛批一顿？神秘的东方力量会给你答案...

## 如何开始

克隆项目，并激活Python虚拟环境：

```bash
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
```

安装依赖项：
`pip install -r requirements.txt`

从环境变量导入OpenAI账户以及ElevenLabs的API Keys：

```
export OPENAI_API_KEY=<token>
export ELEVENLABS_API_KEY=<eleven-token>
```

## 开启赛博算命！

在命令行直接执行fortune_teller.py:

```bash
python fortune_teller.py
```

