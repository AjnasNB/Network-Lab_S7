#Ajnas is creating a tcp client program to send a message to the server in order to check whether the input is a palindrome or not
# He is using the socket module to create a socket object
import socket
# He is creating a socket object
s=socket.socket()
# He is connecting to the server
adr=('localhost', 5000)
s.connect(adr)
#He is creating a while loop to check whether the input is a palindrome or not
while True:
    # He is taking the input from the user
    message=input("Enter a string(Enter exit to stop): ")
    # He is sending a message to the server
    s.send(message.encode())
    # He is recieving a message from the server
    recieved=s.recv(1024)
    print(f"Recieved from server: {recieved.decode()}")
    # He is closing the socket
    if message.lower()=="exit":
        break
# He is closing the socket
    s.close()