#!/usr/bin/env python

"""A demo client for Open Pixel Control
http://github.com/zestyping/openpixelcontrol

Sends red, green, and blue to the first 3 LEDs.

To run:
First start the gl simulator using, for example, the included "wall" layout

    make
    bin/gl_server layouts/wall.json

Then run this script in another shell to send colors to the simulator

    python_clients/example.py

"""

import time
import random
import opc

ADDRESS = '10.0.0.23:6038'
ADDRESS2 = '10.0.0.21:6038'

# Create a client object
client = opc.Client(ADDRESS, verbose=False, protocol="kinet"    )
client2 = opc.Client(ADDRESS2, verbose=False, protocol="kinet"    )

color = 0

# Test if it can connect
if client.can_connect():
    print 'connected to %s' % ADDRESS
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print 'WARNING: could not connect to %s' % ADDRESS

# Send pixels forever
while True:
    #color = (color + 1 ) % 255
    color = 255
    my_pixels = [(color, color, color)] * 255
    #random.shuffle(my_pixels)
    if client.put_pixels(my_pixels):
        print 'sent', color
        client2.put_pixels(my_pixels)
    else:
        print 'not connected'
    time.sleep(0.01)

