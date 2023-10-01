import socket
import cv2
import numpy as np
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'    
port = 12345

client_socket.connect((host, port))
print(f"Connected to the server at {host}:{port}")
cv2.namedWindow("Video Stream", cv2.WINDOW_NORMAL)

while True:
    frame_bytes = client_socket.recv(1024)
    if not frame_bytes:
        break
    frame = cv2.imdecode(np.frombuffer(frame_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow("Video Stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
client_socket.close()
cv2.destroyAllWindows()
