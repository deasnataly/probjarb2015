import socket
import string
import select
import sys

def getNamebySocket(socket):
	
	indeks = Sockets.index(socket)
	senderName = Clients[indeks]
	return str(senderName)

def broadcast_data (sock, msg):	#sock : socket si pengirim data
	
	senderName = getNamebySocket(sock)
	message = '\r<' + senderName + '> ' + msg + '\n'
	
	for socket in Sockets :
		if socket != sock_server and socket!= sock :
			socket.send(message)
		

def storeNewClientData ( newClient_socket ):
	
	newClient_name = newClient_socket.recv(LIMIT)
	Clients.append(newClient_name)
	Sockets.append(newClient_socket)
	#notification
	print newClient_name +' sekarang terhubung ke server.'
	broadcast_data (sockfd, '\r' + newClient_name + ' sekarang terhubung ke server.\n')
	
def client_isOffline ( off_socket ):
	
	off_name = getNamebySocket(off_socket)
	print off_name+' terputus dari server.'
	broadcast_data (sockfd, '\r' + off_name + ' terputus dari server.\n')
	Clients.remove(off_name)
	Sockets.remove(off_socket)

# THE MVP
# kill -9 $(ps aux | grep '[p]ython' | awk '{print $2}')


#main function
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
	Clients.append('server')
	Sockets.append(sock_server)
	print "\nServer terhubung ke jaringan ! Port server : " + str(PORT)
	
	while True:
		read_sockets, write_sockets, error_sockets = select.select(Sockets,[],[])
			
		for sock in read_sockets:
			if sock == sock_server : 
				sockfd, addr = sock_server.accept()
				storeNewClientData(sockfd)
			else :
				msg = sock.recv(LIMIT)
				if msg :
					if msg =='exit' :
						client_isOffline(sock) #kirim data socket client yang exiting
					else :
						broadcast_data(sock, msg)
					
					
	sock_server.close()
	sys.exit()
