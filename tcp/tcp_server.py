#Ajnas is creating a tcp server program to check whether the input is a palindrome or not
# He is using the socket module to create a socket object
import socket
# He is creating a socket object
s=socket.socket()
# He is binding the socket to the port
adr=('localhost', 5000)
s.bind(adr)
# He is listening for connections
s.listen()
print("Waiting for connections...")
# He is accepting the connections using while loop
while True:
    # He is accepting the connections
    c, addr=s.accept()
    print(f"Connected to {addr}")
    # He is recieving a message from the client
    recieved=c.recv(1024)
    # He is decoding the message
    message=recieved.decode()
    print(f"Recieved from client: {message}")
    # He is checking whether the input is a palindrome or not
    if message.lower()=="exit":
        c.send("Goodbye!".encode())
        break
    elif message==message[::-1]:
        c.send("The input is a palindrome".encode())
        print("The input is a palindrome")
    else:
        c.send("The input is not a palindrome".encode())
        print("The input is not a palindrome")
    # He is closing the connection
s.close()