import zmq

# Create context
context = zmq.Context()
# Create socket
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5000")

# Send request for quote
socket.send(b"Quote please!")

# Receive quote
message = socket.recv_string()
print(message)
