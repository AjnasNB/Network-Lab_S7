# Ajnas is creating a client for Caesar decryption
# importing socket module
import socket

# defining function for Caesar decryption
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

# creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# connecting to server
s.connect(('localhost', 9999))
print("Connected to the server")

# sending data to server
input_data = input("Enter data to send to the server: ")
s.send(input_data.encode())

# receiving data from server
result = s.recv(1024).decode()
print("Data received from the server is: " + result)

# calling Caesar_decrypt function
data = caesar_decrypt(result, 4)
print("Decrypted data is: " + data)

if data == input_data:
    print("Data is successfully decrypted")
else:
    print("Data is not successfully decrypted")

# closing socket
s.close()
