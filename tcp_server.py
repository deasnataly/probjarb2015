import socket
import string
import select
import sys

def broadcast_data (sock, message):
	#sock : identitas pengirim
	for socket in SOCKETS_ARRAY :
		if socket != sock_server and socket!= sock :
			try :
				socket.send(message)
			except : #broken socket
				raise 

#def storeNewClientData(socket, username)
	

#def private_msg(sockFrom, sockTo, msg) :

# THE MVP
# kill -9 $(ps aux | grep '[p]ython' | awk '{print $2}')


#main function
if __name__ == "__main__" :
	
	SOCKETS_ARRAY = []
	LIMIT = 4096
	HOST = "0.0.0.0"
	PORT = 5000
	
	sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#has no effect? kenapa?
	
	sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock_server.bind((HOST, PORT))
	sock_server.listen(10)
	
	
	#add server ke dalam array sockets
	SOCKETS_ARRAY.append(sock_server)
	print "\nServer terhubung ke jaringan ! Port server : " + str(PORT)
	
	while True:
		read_sockets, write_sockets, error_sockets = select.select(SOCKETS_ARRAY,[],[])
			
		for sock in read_sockets:
			if sock == sock_server : 
				sockfd, addr = sock_server.accept()
				SOCKETS_ARRAY.append(sockfd)
				print "Client dengan detail (%s, %s) terhubung" %addr
				broadcast_data(sockfd, "Client (%s, %s)  terhubung ke jaringanmu!" %addr)
			
			else :
				# tes mungkin ada data masuk
				try :
					data = sock.recv(LIMIT)
					if data :
						if(data=='exit') :
							print "Client dengan detail (%s, %s) terputus" %addr
							SOCKETS_ARRAY.remove(sock)
							broadcast_data(sock,"Client " + str (sock.getpeername()) + " terputus dari server\n" )
							sock.close()

						else :
							broadcast_data(sock, "\r" + '<' + str (sock.getpeername()) + '>' + data )
				except :
					continue
					
	sock_server.close()
	sys.exit()
				
				
				
