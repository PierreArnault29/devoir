import socket
import codecs
UDP_IP= "10.160.108.101"
UDP_PORT= 5005
tab=[]
data='cinema'
cle=''



#sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#data, addr = sock.recvfrom(1024)
#tab=data
#cle=(str(tab[0])+str(tab[1])+str(tab[2])+str(tab[3]))
#sock.sendto(cle.encode(),(UDP_IP, UDP_PORT))
#print(cle)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(data.encode(),(UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)
print(data)
tab=data
cle=(str(tab[0])+str(tab[1])+str(tab[2])+str(tab[3]))
sock.sendto(cle.encode(),(UDP_IP, UDP_PORT))

print(cle)
data, addr = sock.recvfrom(1024)
print(data)



#b8 04 de f7
#184 4 222 247
#1011 1000 0000 0100 1101 1110 1111 0111
#111110111 10111000 01000000 11011110

#b4 14
