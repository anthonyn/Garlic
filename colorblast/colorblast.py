#!/usr/bin/python2
import time
import random
import opc



#I think these are the right addresses..., might be 22, 23 and 24.
#They are labled in tape on teh sid eof the box
ADDRESS1 = '10.0.0.21:6038'
ADDRESS2 = '10.0.0.22:6038'
ADDRESS3 = '10.0.0.23:6038'


client1 = opc.Client(ADDRESS1, verbose=False, protocol="kinet")
client2 = opc.Client(ADDRESS2, verbose=False, protocol="kinet")
client3 = opc.Client(ADDRESS3, verbose=False, protocol="kinet")

clients = [client1, client2, client3]

# for client in clients:
# 	print client.protocol

# Test if it can connect
if client1.can_connect():
    print 'connected to %s' % ADDRESS1
else:
    print 'WARNING: Client1 could not connect to %s' % ADDRESS1

if client2.can_connect():
    print 'connected to %s' % ADDRESS2
else:
    print 'WARNING: Client 2 could not connect to %s' % ADDRESS2

if client3.can_connect():
    print 'connected to %s' % ADDRESS3
else:
    print 'WARNING: Client3 could not connect to %s' % ADDRESS3



# Send pixels forever
while True:
    #color = (color + 1 ) % 255
    
    color = 255
    my_pixels = [(color, color, color)] * 255

    for client in clients:
    	#random.shuffle(my_pixels)
    	if client.put_pixels(my_pixels):
        	print 'sent', color
    	else:
        	print 'not connected'
    # if client2.put_pixels(my_pixels):
    #     print 'sent', color
    # else:
    #     print 'not connected'
    # if client3.put_pixels(my_pixels):
    #     print 'sent', color
    # else:
    #     print 'not connected'      


    #tune the sleep here          
    time.sleep(0.1)

