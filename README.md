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

# TODO
- Make it so you can ban/kick users from the C&C
- Make it so you can edit your messages via client.py and the C&C
- Have a bot with many features such as anti-swearing, advance anti-spam, etc.
- Have a PM system
In the works:
- User online system


That is all, here are some screen shots:
# C&C:
![Alt text](/cnc1.png?raw=true "Title")
![Alt text](/cnc2.png?raw=true "Title")

# Client
http://prntscr.com/otm643
http://prntscr.com/otm6rz
