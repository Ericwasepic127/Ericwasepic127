# Hi there 👋 

***Hello for anyone reading this! My name is Erkhembayar Batjargal (Батжаргалын Эрхэмбаяр) and I'm 12 years old (13 in December)! I'm Mongolian.***

# [A link to my website](ericwasepic127.github.io)
Thanks for visiting!

## My favourite creations:

- [log-the-app](https://github.com/Ericwasepic127/log-the-app) **A logging utility for Python** ![GitHub last commit](https://img.shields.io/github/last-commit/Ericwasepic127/log-the-app) ![GitHub stars](https://img.shields.io/github/stars/ericwasepic127/log-the-app)
- [simple-server](https://github.com/Ericwasepic127/simple-server) **A super simple server application has GUI** ![GitHub last commit](https://img.shields.io/github/last-commit/Ericwasepic127/simple-server) ![GitHub stars](https://img.shields.io/github/stars/ericwasepic127/simple-server)
- [py3repl](https://ericwasepic127.github.io/hello.html) **Python In Browser!** ![GitHub last commit](https://img.shields.io/github/last-commit/Ericwasepic127/ericwasepic127.github.io) ![GitHub stars](https://img.shields.io/github/stars/ericwasepic127/ericwasepic127.github.io)
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
        file.write(data)
    ```
2. After load, import it
  * Import just as `import m2w`
3. If it's on ...
  - ***Main**, then use*
    `connect = m2w.Main()`
  - ***Worker**, then use*
    `connect = m2w.Worker()`
4. ***Send messages using*** `connect.sendmsg(Message_here)` and recieve using `connect.getmsg`
