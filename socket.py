'''
Created on Mar 13, 2014

@author: siddharthmehta
'''
import socket
import sys
 
try:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
host = 'www.comeze.com'
port = 80 
#ipadd="127.0.0.1"
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
s.connect_ex((remote_ip,port))
print 'socket connected to ' + host + ' on ' + remote_ip
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    s.sendall(message)
except socket.error:
    print 'Send failed'
    sys.exit()
 
print 'Message sent successfully'
reply = s.recv(4096);
print reply


s.close()
