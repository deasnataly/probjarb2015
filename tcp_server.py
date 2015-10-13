import socket
import string
import select
import sys
from datetime import date,datetime

# [NEW_USR]
# [USR_OFF]
# [NEW_GPC]
# [GPC_OFF]
# [ASK_ONU]
# datetime : datetime.now().strftime("%H:%M:%S, %d:%m:%y")

def nameExists(name) :
	if name in Clients :
		return True
	else :
		return False

def getNamebySocket(socket):
	indeks = Sockets.index(socket)
	senderName = Clients[indeks]
	return str(senderName)

def getSocketbyName(name):
	indeks = Clients.index(name)
	socket = Sockets[indeks]
	return socket

def broadcast_data (sock, msg):	#sock : socket si pengirim data
	senderName = getNamebySocket(sock)
	message = '\r' + senderName + ': ' + msg + '\n'
	for socket in Sockets :
		if socket != sock_server and socket!= sock :
			socket.send(message)

def privateMsg(sockFrom, nameTo, msg):
	senderName = getNamebySocket(sockFrom)
	if msg == False or msg == None or msg == '' or msg == '\n' :
		msg = ' mengirimkan sebuah pesan kosong.'
		
	if nameTo in Clients :
		message = '\r[PrivateMessage] from ' + senderName + ' : ' + msg + '\n'
		sockTo = getSocketbyName(nameTo)
		if sockTo == sockFrom :
			sockFrom.send('\r[Warning] You are sending to yourself an empty message, its prohibited!\n')
		else :
			sockTo.send(message)
	else :
		sockFrom.send('\r[Error] Username yang dituju belum terdaftar\n')

def storeNewClientData ( newClient_socket, newClient_name ):
	Clients.append(newClient_name)
	Sockets.append(newClient_socket)
	#notification
	print datetime.now().strftime("%H:%M:%S, %d:%m:%y") +' [NEW_USR] '+  newClient_name +' sekarang terhubung '
	
	broadcast_data (sockfd, '\r[NEW_USR] ' + newClient_name + ' sekarang terhubung ke server.')
	
	
def client_isOffline ( off_socket ):
	off_name = getNamebySocket(off_socket)
	Sockets.remove(off_socket)
	print datetime.now().strftime("%H:%M:%S, %d:%m:%y") +' [USR_OFF] ' + off_name +' terputus dari server.'
	broadcast_data (sockfd, '\r[USR_OFF] ' + off_name + ' terputus dari server.')
	Clients.remove(off_name)
	

def listClients( sockRequested ):
	print datetime.now().strftime("%H:%M:%S, %d:%m:%y") +' [ASK_ONU] '  + getNamebySocket(sockRequested) +' meminta user online.'
	sockRequested.send('\r    List User Online')
	for client in Clients :
			sockRequested.send('\r    Online : ' + client)

		

# THE MVP !
# kill -9 $(ps aux | grep '[p]ython' | awk '{print $2}')

if __name__ == "__main__" :
	
	Clients = [] #array of clients name
	Sockets = [] #array of sockets
	
	LIMIT = 4096
	HOST = "0.0.0.0"
	PORT = 5000
	sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse address
	sock_server.bind((HOST, PORT))
	sock_server.listen(10)
	
	Clients.append('Pengawas')
	Sockets.append(sock_server)
	print "\nServer terhubung ke jaringan ! Port server : " + str(PORT)
	
	while True:
		read_sockets, write_sockets, error_sockets = select.select(Sockets,[],[])
			
		for sock in read_sockets:
			if sock == sock_server : 
				sockfd, addr = sock_server.accept()
				
				gogo = False
				while gogo!=True :
					uname = sockfd.recv(LIMIT)
					if uname!=None and uname!=False :
						if uname in Clients :
							sockfd.send('false')
						else :
							sockfd.send('true')
							storeNewClientData(sockfd, uname)
							gogo=True
							
			else :
				msg = sock.recv(LIMIT)
				if msg :
					if msg =='exit' :
						client_isOffline(sock) #kirim data socket client yang exiting
					else :
						arrayMsg = msg.split(' ',2)
						if arrayMsg[0]=='pm' :
							nameTo = arrayMsg[1]
							privateMsg(sock, nameTo, arrayMsg[2] )
						elif arrayMsg[0]=='listuser' :
							listClients(sock)
						elif arrayMsg[0]=='whoami' :
							sock.send('\r' + getNamebySocket(sock) +'\n')
						else :
							broadcast_data(sock, msg)
	sock_server.close()
	sys.exit()
