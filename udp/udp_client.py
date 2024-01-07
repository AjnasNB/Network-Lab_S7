# Ajnas is creating a udp client program to check whether the input is an amstrong number or not
# He is importing the socket module
import socket
# He is creating a socket object
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# He is taking the input from the user
num=int(input("Enter a number: "))
# He is converting the number into string
num=str(num)
# He is sending the number to the server
adr=('localhost', 1234)
s.sendto(num.encode(), adr)
# He is receiving the result from the server
result=s.recvfrom(1024)
# He is printing the result
print(result[0].decode())
# He is closing the socket
s.close()

