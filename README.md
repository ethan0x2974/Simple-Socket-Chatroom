# Simple-Socket-Chatroom
A simple chatroom using Python 3 and the sockets module.

This chatroom uses two files in order to work:
- Client.py (This is the file to connect and chat)
- Server.py (This is the file to start the C&C server which the client uses to work)

This chatroom works for windows only right now, but to make it work for all OS's you just need to remove the ctype refernces.

Modules being used:
'import socket
import select
from colorama import init, Fore, Back, Style
from time import gmtime, strftime
import os
import time
import ctypes'

