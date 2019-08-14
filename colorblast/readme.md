https://www.raspberrypi.org/documentation/linux/usage/systemd.md


https://tecadmin.net/setup-autorun-python-script-using-systemd/


https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython


THe pi has a python scrip called colorblast.py that runs as a service.  It should connect to the three colorblasts and send forever.  The service is called garlic


sudo systemctl status garlic.service 



There is a function to cycle through a rainbow, and a varible you can change to speed it up or slow it down.  Right now its 1, it can have a decimal.
