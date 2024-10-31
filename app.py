import socket

def start_server(host='127.0.0.1', port=8080):
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    while True:
        # Accept client connection
        client_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address}')

        # Receive client request
        request = client_socket.recv(1024).decode()
        print(f'Request: {request}')

        # Simple HTTP response
        response = """HTTP/1.1 200 OK
Content-Type: text/html

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
"""
        client_socket.sendall(response.encode())
        client_socket.close()

if __name__ == '__main__':
    start_server()
