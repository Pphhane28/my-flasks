from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Your Full Name"
    username = os.getlogin()
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # Get top command output
    top_output = subprocess.getoutput('top -b -n 1')
    
    return f'''
    <h1>HTop Info</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    '''

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=8000)