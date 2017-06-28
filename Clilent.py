import socket
import sys
import struct
import time

#main funtion

if __name__  ==' main ':
    if len(sys.argv)<2:
        print 'Usage : python client.py hostname'
        sys.exit()

host = ''#sys.argv[1]
port = 8888

#create an INET,STREAMing socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()


print 'Socket Create'

try:
    remote_ip = socket.gethostbyname(host)
    s.connect((host,port))
except socket.gaierror:
    print 'Hostname could not be resovolved. Exiting'
    sys.exit()

print 'Socket Connected to ' + host +'on ip' + remote_ip

#Send some data to remote server



#def getuserinput():
    #message = raw_input('Enter your data  !')
    
    


try:
    #set the whole string
    #message1=getuserinput()
    while True:
        message = raw_input('Enter your data  !\n')
        s.send(message)
        print 'Message sent successfully'
        time.sleep(1)
        #s.recv(1024)
        print s.recv(1024)
        #print 'Sending...'
        time.sleep(2)
    
        

except socket.error:
    #Send Failed
    print 'Send Failde'
    sys.exit()


def recv_timeout(the_socket,timeout=2):
    #make socket non blocking

    the_socket.setblocking(0)

    #total data partwise in an array
    total_data=[];
    data='';
    #beginning time
    begin=time.time()
    while 1:
        #if you got somet data,then break after timeout
        if total_data and time.time()-begin > timeout:
            break

        #if you got no data at all,wait a little longer twice the timeout
        elif time.time()-begin>timeout*2:
            break

        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin=time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass

s.close()
    
