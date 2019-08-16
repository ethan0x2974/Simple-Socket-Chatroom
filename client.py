import errno
import sys
import socket
import select
from colorama import init, Fore, Back, Style
from time import gmtime, strftime
import os
import time
import ctypes

os.system('cls')

init(convert=True)

useron = '0'

HL = 10
IP = "127.0.0.1"
PORT = 1337

ctypes.windll.kernel32.SetConsoleTitleW("Welcome to the chatroom | Connected to" + f" {IP} on port {PORT}")
print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.GREEN + " Connection with server established." + Fore.WHITE)

my_username = input("Enter your username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
uh = f"{len(username):<{HL}}".encode('utf-8')

client_socket.send(uh + username)

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Connecting to" + f" {IP} on port {PORT}.")
print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.MAGENTA + " Connecting." + Fore.WHITE)
time.sleep(.75)
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Connecting to" + f" {IP} on port {PORT}..")
print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.MAGENTA + " Connecting.." + Fore.WHITE)
time.sleep(.75)
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Connecting to" + f" {IP} on port {PORT}...")
print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.MAGENTA + " Connecting..." + Fore.WHITE)
time.sleep(.75)
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Connecting to" + f" {IP} on port {PORT}.")
print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.MAGENTA + " Connecting." + Fore.WHITE)
time.sleep(.75)
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Connecting to" + f" {IP} on port {PORT}..")
print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.MAGENTA + " Connecting.." + Fore.WHITE)
time.sleep(.75)
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Connecting to" + f" {IP} on port {PORT}...")
print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.MAGENTA + " Connecting..." + Fore.WHITE)
time.sleep(.75)
os.system("cls")


print(f"["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"]" + Fore.GREEN + " Successfully logged in to chatroom. Welcome, " + Fore.YELLOW + my_username + Fore.WHITE)
useron =+ 1
ctypes.windll.kernel32.SetConsoleTitleW(f"Welcome to the chatroom, {my_username}")

while True:
	
	message = input(f"["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"] > " )

	if message:
		message = message.encode('utf-8')
		message_header = f"{len(message):<{HL}}".encode('utf-8')
		client_socket.send(message_header + message)

	try:
		while True:
			uh = client_socket.recv(HL)
			if not len(uh):
				print("["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"] "+ Fore.RED +"Connection closed by the sever"+ Fore.WHITE)
				sys.exit()

			username_length = int(uh.decode('utf-8').strip())
			username = client_socket.recv(username_length).decode('utf-8')

			message_header = client_socket.recv(HL)
			message_length = int(message_header.decode('utf-8').strip())

			message = client_socket.recv(message_length).decode('utf-8')

			print(f"["+Fore.CYAN+strftime("%H:%M:%S", gmtime())+Fore.WHITE+"] " + Fore.MAGENTA + username +Fore.WHITE+ ": "+ Fore.CYAN + message + Fore.WHITE)


	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print("Unknown error", str(e))
			sys.exit()
		continue	

	except Exception as e:
		print(f"Unknown error:{str(e)}")
