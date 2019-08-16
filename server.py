import socket
import select
from colorama import init, Fore, Back, Style
from time import gmtime, strftime
import os
import time
import ctypes

os.system('cls')

useron = '0'

init(convert=True)

HL = 10
IP = "127.0.0.1"
PORT = 1337

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()


sockets_list = [server_socket]

clients = {}

ctypes.windll.kernel32.SetConsoleTitleW(f"Chatroom C&C")

print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.GREEN + " C&C Server Started on " + Fore.WHITE + IP + Fore.GREEN + " using port " + Fore.WHITE + f"{PORT}")

def receive_message(client_socket):
	try:
		message_header = client_socket.recv(HL)

		if not len(message_header):
			return False

		message_length = int(message_header.decode('utf-8'))
		return {"header" : message_header, "data" : client_socket.recv(message_length)}

	except Exception as e:
		return False


while True:
	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

	for notified_socket in read_sockets:
		if notified_socket == server_socket:
			client_socket, client_address = server_socket.accept()

			user = receive_message(client_socket)
			
			if user is False:
				continue

			sockets_list.append(client_socket)
			clients[client_socket] = user
            

			



			print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.GREEN + " New connection from" + Fore.WHITE + f" {client_address[0]}:{client_address[1]}" + Fore.GREEN + " Using the username: " + Fore.WHITE + f"{user['data'].decode('utf-8')}")

		else:
			message = receive_message(notified_socket)
			if message is False:
				print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + f" {clients[notified_socket]['data'].decode('utf-8')}" + Fore.RED + " left the chatroom" + Fore.WHITE)
				sockets_list.remove(notified_socket)
				del clients[notified_socket]
				continue

			user = clients[notified_socket]
			print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"] New message from " + f"{user['data'].decode('utf-8')}" + f": {message['data'].decode('utf-8')}")



			for client_socket in clients:
				if client_socket != notified_socket:
					client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])



	for notified_socket in exception_sockets:
		sockets_list.remove(notified_socket)
		del clients[notified_socket]



