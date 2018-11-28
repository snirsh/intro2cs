###########
# Imports #
###########
import socket

#############
# Constants #
#############

HOST = 'e-intro.cs.huji.ac.il'  # a special
# reserved name which represent
# the network address of current computer
PORT = 8000  # Arbitrary choice
MAXIMUM_NUMBER_OF_QUEUED_CONNECTIONS = 0
MAX_DATA_CHUNK = 1024

########
# Code #
########

s = socket.socket()
s.connect((HOST, PORT))
msg = 'hi'
encoded_msg = bytes(msg,'ascii')
s.sendall(encoded_msg)
data = s.recv(MAX_DATA_CHUNK)
s.close()
print('Received', data)
