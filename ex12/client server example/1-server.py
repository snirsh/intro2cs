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

server_socket = socket.socket()
server_socket.bind((HOST, PORT))
# Waiting for client connections
server_socket.listen(MAXIMUM_NUMBER_OF_QUEUED_CONNECTIONS)
# conn is a new socket object usable
#  to send and receive data on the connection,
# address is the address bound to the
#  socket on the other end of the connection.
(transmission_socket, client_address) = server_socket.accept()
while True:
    encoded_data = transmission_socket.recv(MAX_DATA_CHUNK)

    if not encoded_data:
        # Data transmission ended
        break
    else:
        # Do something with the data
        print(encoded_data.decode('ascii'))
        reply_msg = bytes('Bye', 'ascii')
        transmission_socket.sendall(reply_msg)

transmission_socket.close()
server_socket.close()
