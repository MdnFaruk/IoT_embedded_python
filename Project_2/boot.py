try:
  import usocket as socket
except:
  import socket

import network, esp, gc

esp.osdebug(None)
gc.collect()

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('faruk', 'farukBD33')

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
print('<=====================================>')

# ap = network.WLAN(network.AP_IF)
# ap.active(True)
# ap.config(essid='faruk', password='farukBD33')
# 
# while ap.active() == False:
#   pass
# 
# print(ap.ifconfig())