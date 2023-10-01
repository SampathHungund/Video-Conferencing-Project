import socket
import cv2 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")
cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read() 

    if ret:
        client_socket.send(frame.tobytes())
cap.release()
client_socket.close()
server_socket.close()
