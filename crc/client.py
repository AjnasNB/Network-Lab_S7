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
    bin_reminder=bin(reminder)
    
    print(f"quotient,rem{quotient,reminder}")
    print(f"bin_reminder{bin_reminder}")
    return bin_reminder[2:]

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

while True:
    # Get user input
    message = input("Enter message (type 'exit' to stop): ")

    # Check if the user wants to exit
    if message.lower() == "exit":
        print("Exiting client...")
        client_socket.sendall("exit".encode())
        break

    # Perform CRC on the message
    crc_code = perform_crc(message)

    # Combine the message and CRC code
    data_to_send = f"{message}{crc_code}"
    print(data_to_send)

    # Send the data to the server
    client_socket.sendall(data_to_send.encode())

# Close the connection
client_socket.close()
