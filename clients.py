#telnet program example (?)
import socket, select, string, sys

def prompt() :
	sys.stdout.write('<You> ')
	sys.stdout.flush()

#def registrate() :
#	sys.stdout.write('Masukkan username anda : ')
#	username = sys.stdin.readline()
#	if not msg : #username berupa whitespace
#		sys.stdout.write('[Error] Username harus berupa string\n')
#	s.send(msg)
	
	
#main function
if __name__ == "__main__" :
	
	if(len(sys.argv) < 3): #kalau jumlah kata yang di enter di python kurang dari 3
		print ' Cara menggunakan : python clients.py <hostname> <port>\n'
		sys.exit()
		
	host = sys.argv[1]
	port = int (sys.argv[2])
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.settimeout(2)
	
	try :
		s.connect((host, port))
	except :
		print 'Tidak bisa konek, host anda mungkin tidak aktif atau salah port\n'
		sys.exit()
		
	LIMIT = 4096
	
	
	print 'Terkoneksi ke server. Ketik pesan anda!\n'
	prompt()
	
	
	while True:
		list_socket = [sys.stdin, s]
		read_sockets, write_sockets, error_sockets = select.select(list_socket, [], [])
		
		for sock in read_sockets :
			if sock == s : #ada pesan masuk dari server
				data = sock.recv(LIMIT)
				if not data :
					sys.stdout.write('Terputus dari server chat\n')
					break
				else :
					sys.stdout.write(data) #print data
					prompt()
				
			else : #user memasukkan pesan
				msg = sys.stdin.readline()
				
				if str(msg.rstrip('\n')) =='exit' :
					s.send('exit')
					sys.stdout.write('Memutuskan sambungan ke server...\n')
					sys.exit()
					
				else :
					s.send(msg) #mengirim pesan...
					prompt()
					
	sys.exit()
		
		
