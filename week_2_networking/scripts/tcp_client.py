import socket

# Connect to local TCP server
target_host = "127.0.0.1"
target_port = 9999

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send a simple message
message = "Hello Server"
client.sendall(message.encode())

# Receive response
response = client.recv(4096)

print(response.decode())