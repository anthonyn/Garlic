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


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    # if pos < 0 or pos > 255:
    #     r = g = b = 0
    if pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) 


#Leave this its the index value for the rainbow
i = 0


#make this bigger and smaller to control transistion speed
waitTime = 1

#replace color with a simple R G B value if you want static colors
# like this [(255,0,0)]

# Send pixels forever
while True:
    #color = (color + 1 ) % 255
    
    i = (i + 1 ) % 255 
    color = wheel(i)
    my_pixels = [color] * 255

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
    time.sleep(waitTime)

