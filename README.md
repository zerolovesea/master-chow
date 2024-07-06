# Master Chow: Your Cyber Fortune Teller
**This project is inspired by [narrator: David Attenborough narrates your life](https://github.com/cbh123/narrator), thanks to the original author's contribution.**

![](assets/bagua.jpg)

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README_CN.md">简体中文</a> |
</p>

## Want to know your fortune for today? Let Master Zhou take a look:>

Will today be smooth sailing at work? The mysterious power of the East will give you the answer...

## How to Get Started

Clone the project and activate Python virtual environment:

PS:The Python version should be 3.11 or later.

```bash
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
```

Install dependencies:
`pip install -r requirements.txt`

Import your OpenAI account and ElevenLabs API Keys from environment variables:

```
export OPENAI_API_KEY=<token>
export ELEVENLABS_API_KEY=<eleven-token>
```

## Start the Cyber Fortune Telling!

Run fortune_teller.py directly from the command line:

```bash
python fortune_teller.py
```
