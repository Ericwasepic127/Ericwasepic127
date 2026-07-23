# 📱 I love to use android!

***Because Android was open!** [But does they?](https://keepandroidopen.org/)*

# Hi there 👋 

![Profile views count](https://komarev.com/ghpvc/?username=ericwasepic127&color=red&abbreviated=true)
![GitHub followers count](https://img.shields.io/github/followers/ericwasepic127)

![My GitHub streak](https://github-readme-streak-stats.herokuapp.com/?user=ericwasepic127&theme=radical)

***Hello for anyone reading this! My name is Erkhembayar Batjargal (Батжаргалын Эрхэмбаяр) and I'm 12 years old (13 in December)! I'm Mongolian.*** 

# [A link to my website](https://ericwasepic127.github.io/)
Thanks for visiting!
![My logo here!](https://ericwasepic127.github.io/logo.png)

## My favourite creations:

- [log-the-app](https://github.com/Ericwasepic127/log-the-app) **A logging utility for Python** ![GitHub last commit](https://img.shields.io/github/last-commit/Ericwasepic127/log-the-app) ![GitHub stars](https://img.shields.io/github/stars/ericwasepic127/log-the-app)
- [simple-server](https://github.com/Ericwasepic127/simple-server) **A super simple server application has GUI** ![GitHub last commit](https://img.shields.io/github/last-commit/Ericwasepic127/simple-server) ![GitHub stars](https://img.shields.io/github/stars/ericwasepic127/simple-server)
- [py3repl](https://ericwasepic127.github.io/hello.html) & [py3ide](https://ericwasepic127.github.io/ide.html) **Python In Browser!** ![GitHub last commit](https://img.shields.io/github/last-commit/Ericwasepic127/ericwasepic127.github.io) ![GitHub stars](https://img.shields.io/github/stars/ericwasepic127/ericwasepic127.github.io)
- [m2w](./m2w.py) **PyScript Simple Main to Worker and Worker to Main connection API - Look below for more information**

## Don't miss MongolOS! @MongolOS1162 [MongolOS Official Site](https://mongolos1162.github.io/)

## If you got questions to me, 

**... you can feel free to ask - Just make issue in this repo!**

# Details about some projects
## PyScript m2w
### A simple API handles worker & main thread communication in PyScript
How to use?
1. On main.py and worker.py, load up m2w.py
  * m2w loading tip:
    ```python
    import pyscript, asyncio
    data = asyncio.run(pyscript.fetch("https://raw.githubusercontent.com/Ericwasepic127/Ericwasepic127/refs/heads/main/m2w.py"))
    with open("m2w.py", "w") as file:
        if data.ok:
            file.write(asyncio.run(data.text()))
    ```
2. After load, import it
  * Import just as `import m2w`
3. If it's on ...
  - ***Main**, then use*
    `connect = m2w.Main()`
  - ***Worker**, then use*
    `connect = m2w.Worker()`
4. ***Send messages using*** `connect.sendmsg(Message_here)` and recieve using `connect.getmsg`
## safeATM - Simple minigame of Cybersecurity!
### What it is?
- It is a simple game written in Python, and simulates ATM working
Attackers will try to scam your ATM! Create Rules to protect it! **Also don't block regular users too!**
### How to run?
- You can run this without installing python, download the [safeATM.py](./safeATM.py), open https://ericwasepic127.github.io/ide.html and click at `Upload code from storage`. Then click `Run` when it's available to click, and follow instructions on screen!
If you have local environment, download the [safeATM.py](./safeATM.py) and run as `python3 safeATM.py`
