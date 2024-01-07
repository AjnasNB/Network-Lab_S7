# Ajnas is creating a client program to send a message to the server
# He is using the socket module to create a socket object
import socket
# He is creating a socket object
adr=('localhost', 5000)
s=socket.socket()
# He is connecting to the server
s.connect(adr)
# He is sending a message to the server
message="Hello, server! I am client."
s.send(message.encode())
# He is recieving a message from the server
recieved=s.recv(1024)
print(f"Recieved from server: {recieved.decode()}")
# He is closing the socket
s.close()