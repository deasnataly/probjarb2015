import socket, select

def broadcast_data (sock, message):

	for socket in SOCKETS_ARRAY :
		if socket != sock_server and socket!= sock :
			try :
				socket.send(message)
			except : #broken socket
				raise ValueError


def private_msg (sockFrom, sockTo, msg) :
	if sockFrom != sock_server and sockTo !=sock_server and sockFrom != sockTo :
		try :
			sockTo.send(msg)
		except :
			
			sockTo.close()
			
	else :
		print '[Error] Mengirim ke server atau mengirim ke diri sendiri tidak diperbolehkan! \n'

#main function
if __name__ == "__main__" :
	
	SOCKETS_ARRAY = []
	LIMIT = 4096
	PORT = 5002
	
	sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#has no effect? kenapa?
	
	sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock_server.bind(("127.0.0.1", PORT))
	sock_server.listen(10) #limit koneksi
	
	
	#add server ke dalam array sockets
	SOCKETS_ARRAY.append(sock_server)
	print "Server terhubung ke jaringan ! Port server : " + str(PORT)
	
	while 1:
		#cari list sockets yang ready untuk dibaca lewat:
		read_sockets, write_sockets, error_sockets = select.select(SOCKETS_ARRAY,[],[])
		
		for sock in read_sockets:
			if sock == sock_server : #ada koneksi baru yang socketnya sama dengan server socket
				sockfd, addr = sock_server.accept()
				SOCKETS_ARRAY.append(sockfd)
				print "Client dengan detail (%s, %s) terkoneksi\n" %addr
				broadcast_data( sockfd, "(%s, %s) Client terkoneksi ke jaringanmu! \n" %addr)
			
			else :
				# tes mungkin ada data masuk
				try :
					data = sock.recv(LIMIT)
					if data:
						broadcast_data(sock, "\r" + '<' + str (sock.getpeername()) + '>' + data )
				except :
					#TODO : VAR ADDR DATANGNYA DARI MANAAAA ~~~
					print "Client dengan detail (%s, %s) terputus\n" %addr
					broadcast_data(sock,"Client dengan detail (%s, %s) terputus\n" %addr)
					sock.close()
					SOCKETS_ARRAY.remove(sock)
					continue
					
	sock_server.close()
				
				
				
