# Ajnas creating a server for Caesar encryption
# importing socket module
import socket

# defining function for Caesar encryption
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# binding socket to port
s.bind(('localhost', 9999))
print("Socket bound to port 9999")

# putting socket in listening mode
s.listen(5)
print("Socket is listening")

# accepting connection
client_socket, addr = s.accept()
print("Connection accepted from " + str(addr))

# receiving data from the client
data = client_socket.recv(1024).decode()
print("Data received from client is: " + data)

# calling Caesar_encrypt function
result = caesar_encrypt(data, 4)

# sending encrypted data to the client
client_socket.send(result.encode())

# closing socket
s.close()
