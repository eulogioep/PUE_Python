# # Conectarse a un servidor http

# import socket

# #server_addr = input("What server do you want to connect to? ")
# server_addr = 'example.com'
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))

# # Solicitud de un documento al server
# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")
# reply = sock.recv(10000)

# # Cierra la conexión con el server.
# sock.shutdown(socket.SHUT_RDWR)
# sock.close()

# # Imprimir la respuesta
# print(repr(reply))

###########################################################

# Conexión y parseo de la respuesta a un server http.

# import socket

# def parse_response(response):
#     headers, _, body = response.partition('\r\n\r\n')
#     status_line, * headers_lines = headers.split('\r\n')
#     status_code = int(status_line.split()[1])

#     return status_code, headers_lines, body

# server_addr = 'example.com'
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((server_addr, 80))

# print("\nGET / HTTP/1.1\r\n" + 
#       "Host: " + server_addr +
#       "\r\nConnection: close\r\n\r\n")

# sock.send(b"GET / HTTP/1.1\r\nHost: " +
#           bytes(server_addr, "utf8") +
#           b"\r\nConnection: close\r\n\r\n")

# response = sock.recv(10000)
# status_code, headers, body = parse_response(response.decode())

# print(f"Status Code: {status_code}")
# print("\nHeaders:")
# for header in headers:
#     print(header)
# print("\nBody:")
# print(body)

#########################################################



