
def handle_client(client_socket,file,size,noc):
    j=1
    f=open(file,'rb')
    f.seek(size*(noc-1))
    while(size>1024):
        #client_socket.send(r)
        #j=j+1
        r=f.read(1024)
        size=size-1024
        client_socket.send(r)
        j=j+1
    r=f.read(size)
    client_socket.send(r)
    j=j+1
    print 'done sending'
    print j
    print 'packets'
    client_socket.close()
    f.close()

def file_join(file):
    i=0
    f=file+".mkv"
    q=open(f,"ab")
    while i<8:
        x=file+str(i)+".mkv"
        f=open(x,'rb')
        q.write(f.read())
        f.close()
        i=i+1
    q.close()

def handle_server(file,noc):
    q=file+str(noc)+".mkv"
    f=open(q,'wb')
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    r=s.recv(1024)
    f.write(r)
    k=1
    while(r):
        r=s.recv(1024)
        k=k+1
        f.write(r)
    print 'done receving'
    print k
    print 'packets'
    f.close()
    s.close()






host='localhost'
port=13131
import socket
import threading
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "for server s \nfor client c"
input=raw_input()
if input=='s':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "give file_name"
    file=raw_input()
    temp=open(file,'a')
    size=temp.tell()
    temp.close()
    size=size/8
    size=size+1
    #f=open(file,'rb')
    s.bind((host,port))
    s.listen(8)
    noc=0
    while True:
        client,addr=s.accept()
        print "got connection from ",addr
        noc=noc+1
        client_handler=threading.Thread(target=handle_client,args=(client,file,size,noc,))
        client_handler.start()
        #r=f.read(1024)
        #while (r):
            #client.send(r)
            #i=i+1
            #print "sending\n"
            #r=f.read(1024)
        #print 'done sending '
        #print i
        #print ' packets'
        #break
    s.close()
elif input=='c':
    print "give file_name to save into"
    file=raw_input()
    #f=open(file,'wb')
    noc=0
    while noc<8:
        server_handler=threading.Thread(target=handle_server,args=(file,noc,))
        server_handler.start()
        noc=noc+1
    file_join(file)
    #s.connect((host,port))
    #r=s.recv(1024)
    #f.write(r)
    #i=1
    #while (r):
        #r=s.recv(1024)
        #i=i+1
        #print "receving\n"
        #f.write(r)
    #print 'done receving '
    #print i
    #print ' packets'
    #f.close()
    #s.close()

