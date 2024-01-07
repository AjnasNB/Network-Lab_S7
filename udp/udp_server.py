# Ajnas is creating a udp server program to check whether the input is an amstrong number or not
# He is importing the socket module
import socket
# He is creating a socket object
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# He is binding the socket
adr=('localhost', 1234)
s.bind(adr)
# He is receiving the number from the client
num=s.recvfrom(1024)
# He is converting the number into integer
num=int(num[0].decode())
# He is initializing the sum to zero
sum=0
# He is initializing the temp variable to the number
temp=num
# He is creating a while loop
while temp>0:
    # He is extracting the last digit
    digit=temp%10
    # He is adding the cube of the digit to the sum
    sum+=digit**3
    # He is removing the last digit
    temp//=10
# He is creating an if condition
if num==sum:
    # He is sending the result to the client
    s.sendto("Amstrong".encode(), adr)
    print("Amstrong")
else:
    # He is sending the result to the client
    s.sendto("Not Amstrong".encode(), adr)
    print("Not Amstrong")
# He is closing the socket
s.close()