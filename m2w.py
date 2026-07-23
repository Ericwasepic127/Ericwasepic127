"""
### A simple API handles worker & main thread communication in PyScript
How to use?
1. On main.py and worker.py, load up m2w.py
  * m2w loading tip:
    import pyscript, asyncio
    data = asyncio.run(pyscript.fetch("https://raw.githubusercontent.com/Ericwasepic127/Ericwasepic127/refs/heads/main/m2w.py"))
    with open("m2w.py", "w") as file:
        if data.ok:
           file.write(asyncio.run(data.text()))
2. After load, import it
  * Import just as `import m2w`
3. If it's on ...
  - Main, then use
    `connect = m2w.Main()`
  - Worker, then use
    `connect = m2w.Worker()`
4. Send messages using `connect.sendmsg(Message_here)` and recieve using `connect.getmsg`
"""
import js
from pyodide.ffi import create_proxy

class Main:
    """Main thread only, it will crash in Worker"""
    def __init__(self, id='script[type="py"][terminal]'):
      self.worker = js.document.querySelector(id).xworker
      self.sendmsg = self.worker.postMessage
      self.getmsg = None
      self.msgs = []
      self.id = id
      def on_message(event):
          self.getmsg = event.data
          self.msgs.append(event.data)
      self.worker.onmessage = create_proxy(on_message)

class Worker:
  """Worker thread only, it will send messages to Main in Main"""
  def __init__(self):
      self.worker = js.self
      self.sendmsg = self.worker.postMessage
      self.getmsg = None
      self.msgs = []
      def on_message(event):
          self.getmsg = event.data
          self.msgs.append(event.data)
      self.worker.onmessage = create_proxy(on_message)
