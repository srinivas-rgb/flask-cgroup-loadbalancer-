from flask import Flask
import socket
import psutil
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)
    cpu = psutil.cpu_percent(interval=1)
    return f"""
    <h3>Hello from {hostname}</h3>
    <p>CPU Usage: {cpu:.2f}%</p>
    <p>Memory Usage: {mem:.2f} MB</p>
    """
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

