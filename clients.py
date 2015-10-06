#telnet program example (?)
import socket, select, string, sys

def prompt() :
	sys.stdout.write('<You> ')
	sys.stdout.flush()
	
#main function
if __name__ == "__main__" :
	
	if(len(sys.argv) < 3): #kalau jumlah kata yang di enter di python kurang dari 3
		print ' Cara menggunakan : python clients.py <hostname> <port>\n'
		sys.exit()
		
	host = sys.argv[1]
	port = int (sys.argv[2])
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	s.settimeout(2)
	
	#connect ke remote host
	try :
		s.connect((host, port))
	except :
		print 'Tidak bisa konek, host anda mungkin tidak aktif atau salah port\n'
		sys.exit()
		
	#sukses di try, masuk ke bawah
	LIMIT = 4096
	
	
	print 'Terkoneksi ke server. Ketik pesan anda!\n'
	prompt() #masuk ke fungsi diatas
	
	
	while 1:
		list_socket = [sys.stdin, s]
		#cari list socket yang readable
		read_sockets, write_sockets, error_sockets = select.select(list_socket, [], [])
		
		for sock in read_sockets :
			if sock == s : #ada pesan masuk dari server
				data = sock.recv(LIMIT)
				if not data :
					print '\nTerputus dari server chat\n'
					sys.exit()
				else :
					sys.stdout.write(data) #print data
					prompt()
				
			else : #user memasukkan pesan
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()
				
					
		
		
		
