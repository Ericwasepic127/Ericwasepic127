import subprocess, sys
from tkinter import messagebox as mb
from time import sleep as sp
from threading import Thread as thread
import tkinter as tk
from tkinter.simpledialog import askinteger as minu

def alert(msg, title=__name__, icon=None, extra=None):
    """Simple wrapper handles show popup, made for linux, cross platform compileable
    Arguments:
    - msg: Main message 
    - title: Title
    - icon: Icon to show
    - extra: Adds arguments like --urgent by tuple/list
    Epilog:
    - alert('Hello from Python!', title="Test") # shows Test: Hello from Python!
    - alert('Urgrent test', title='System warning test', extra=['--urgrency=critcal'])
    - alert('Terminal icon', title='Icon test', icon='terminal')
    """
    if not sys.platform.startswith("linux"):
        print("[WARNING]: Skipping icon because it is not Linux\n[WARNING]: Platform is not Linux" if icon is not None else "[WARNING]: Platform is not Linux", file=sys.stderr)
        msgf = lambda: mb.showinfo(title, msg)
        thread(target=msgf, daemon=True).start()
        return 

    cmd = ["notify-send", title, msg]

    if icon is not None:
        cmd += ["-i", icon]
    if extra is not None:
        cmd += extra

    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        raise Exception(f"Something failed: {e}")

def wait(minute=30):
    sec = minute * 60
    for ran in range(sec):
        if sec - ran == 10 * 60:
            alert("10 minutes left!", "10 minutes!")
        if sec - ran == 300:
            alert("5 minutes warning!", "5 minutes!")
        if sec - ran == 60:
            alert("1 MINUTE!!!! HURRY!", "1 MINUTE LEFT")
        if sec - ran == 30:
            alert("30 SECONDS!", "30 seconds countdown", extra=["--urgency=critical"])
        sp(1)

runit = lambda t=30: thread(target=lambda: wait(t), daemon=True).start()

r = tk.Tk()
r.title("Timer")
r.geometry("300x200")
r.resizable(False, False)
tk.Label(r, text="Timer for Anything").pack()
lbl = tk.Label(r, text="Minutes: 30")
lbl.pack()
y = 30

def x():
    global y
    y = minu("Minutes", "Type Minutes to run, defaults to 30 when cancelled or nothing") or 30
    lbl["text"] = f"Minutes: {y}"

def run():
    runit(y)

tk.Button(r, text="Change minutes", command=x).pack()
tk.Button(r, text="Run timer!", command=run).pack()
r.mainloop()
