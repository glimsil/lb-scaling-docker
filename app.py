 
from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    dt = datetime.now()
    html = "<h1>Hello {name}!</h1><br/><b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)