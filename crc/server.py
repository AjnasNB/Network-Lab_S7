import socket

# CRC Key
crc_key = "1011"

# Function to perform CRC
def perform_crc(data):
    divisor = crc_key
    dividend = data + "000"  # Append three zeros for division

    # Perform CRC division
    dividend=int(dividend,2)
    div=int(divisor,2)
    quotient,reminder=divmod(dividend,div)
    print(f"quotient,rem{quotient,reminder}")
    bin_reminder=bin(reminder)
    print(f"bin_reminder{bin_reminder}")
    return bin_reminder[2:]

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening for connections...") 

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()

    # Check if the client wants to exit
    if data.lower() == "exit":
        print("Exiting server...")
        break

    # Separate the message and CRC code
    received_message, received_crc = data[:-3], data[-3:]

    # Perform CRC on the received message
    calculated_crc = perform_crc(received_message)

    # Check if the received CRC matches the calculated CRC
    if '1' not in calculated_crc:
        print(f"Received message: {received_message} (CRC verified)")
    else:
        print("Error in received message (CRC mismatch)")

# Close the connection
client_socket.close()
server_socket.close()
