# Simple-Socket-Chatroom
A simple chatroom using Python 3 and the sockets module.

This chatroom uses two files in order to work:
- Client.py (This is the file to connect and chat)
- Server.py (This is the file to start the C&C server which the client uses to work)

This chatroom works for windows only right now, but to make it work for all OS's you just need to remove the ctype refernces.

Modules being used:
- Colorama
- Socket
- Select
- time
- os
- ctypes

# How to use
first, edit client.py and server.py and change the IP to your server IP or keep it 127.0.0.1 if your running it on your local machine.
you can change the port to any thing you want, just make sure they are the same in both files.
After that run:
`python server.py`
This will start the C&C server.
After the server is running you can now run client.py by doing:
`python client.py`

That is all, here are some screen shots:


