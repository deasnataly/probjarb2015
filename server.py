import threading
import socket
import time
import sys


#Deklarasi kelas
class Server(threading.Thread):
    def __init__(self):
        self.addr = ('localhost', 9090)
        self.servsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.servsocket.bind(self.addr)
        threading.Thread.__init__(self)
        print 'Server is running on %s port %s ' %self.addr

    def openfile(self,nama):
        gigi = open(nama)
        return gigi.read()

    def responding(self):
        #init Thread khusus untuk respons
        # threading.Thread.__init__(self.responding)
        #no need to join thread
        responses = ''
        while True:
            data = self.newConn.recv(32)
            if data:
                responses = responses + data
                if(responses.endswith("\r\n\r\n")):
                    print 'One connection finished their request'
                    self.newConn.send('HTTP/1.1 200 OK \r\n\r\n'+self.openfile('/c/Users/rona/Documents/progjar/progjarb2015/fotoLP.png'))
                    break
        self.newConn.close()

    def run(self):
        self.servsocket.listen(1)
        while True:
            self.newConn , self.connAddress = self.servsocket.accept()
            #handling
            newConnection = self.responding()
            newConnection.start()


newServ = Server()
newServ.start()
