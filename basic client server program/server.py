#Ajnas is creating a server program to recieve a message from the client
# He is using the socket module to create a socket object
import socket
# He is creating a socket object
s=socket.socket()
# He is binding the socket to the address
adr=('localhost', 5000)
s.bind(adr)
# He is listening for connections
s.listen()
print("Server is listening for connections...")
# He is accepting a connection
c,addr=s.accept()
# He is recieving a message from the client
recieved=c.recv(1024)
print(f"Recieved from client with adress {addr} : {recieved.decode()}")
# He is sending a message to the client
message="Hello, client! I am server. Thank you for connecting."
c.send(message.encode())
# He is closing the socket
s.close()