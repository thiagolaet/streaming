import socket, sys, pickle

HOST, PORT = "localhost", 6000
data = { 'message': 'REPRODUZIR_VIDEO', 'user': 1, 'params': {'video_id': 2} }
data_string = pickle.dumps(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(data_string, (HOST, PORT))
received = sock.recv(1024)

response = pickle.loads(received)
print("Sent:     {}".format(data))
print("Received: {}".format(response))