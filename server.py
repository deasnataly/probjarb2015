import threading
import socket
import time
import sys
import os

PORT = 8000

class Respon(threading.Thread):
    def __init__(self, newConn, newAddr,nama):
        self.newConn=newConn
        self.newAddr = newAddr
        self.nama = nama
        print 'nama = ' + self.nama
        threading.Thread.__init__(self)

    def openfile(self,nama):
        ampas = open(nama)
        return ampas.read()

    def routeConnection(self, request):
        splits = request.split(" ")
        pecahkan = splits[1]
        pecahkan = pecahkan[1::]
        responses = 'HTTP/1.1 200 OK\r\n\r\n'
        # self.newConn.send(pecahkan[1::])
        if( str(splits[1]) == '/' ) :
            responses = responses + self.openfile( str('default.jpg'))
        elif os.path.isfile(str(pecahkan)+'.jpg'):
                responses = responses + self.openfile( str(pecahkan)+'.jpg')
        else :
            responses = responses + self.openfile( str('404.jpg'))
        self.newConn.send(responses)

    def run(self):
        response = ''
        while True:
            received = self.newConn.recv(1024)

            if received:
                print 'Received Request = ' + str(received)
                response = response + received
                if(response.endswith("\r\n\r\n")):
                    print 'One connection finished their request'
                    self.routeConnection(received)
                    break
            else :
                break
        self.newConn.close()

#Deklarasi kelas
class Server(threading.Thread):
    def __init__(self):
        self.addr = ('localhost', PORT)
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
                print 'data = ' + str(data)
                print 'responses = ' + str(responses)
                responses = responses + data
                print 'responses = ' + str(responses)
                if(responses.endswith("\r\n\r\n")):
                    self.newConn.send('HTTP/1.1 200 OK \r\n\r\n'+self.openfile('1.jpg'))
                    print 'One connection finished their request'
                    break
        self.newConn.close()

    def run(self):
        self.servsocket.listen(1)
        while True:
            self.newConn , self.connAddress = self.servsocket.accept()
            #handling
#            newConnection = Respon(self.newConn, self.connAddress, 'ampas check')
            newConnection.start()


newServ = Server()
newServ.start()
