from django.shortcuts import render

from django.http import HttpResponse
import os
import time
import subprocess
# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to the Django App</h1><p>Visit /htop for system info.</p>')

def htop(request):
    full_name = "Your Full Name"
    username = os.getlogin()
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    top_output = subprocess.getoutput('top -b -n 1')
    
    return HttpResponse(f'''
    <h1>HTop Info</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    ''')
