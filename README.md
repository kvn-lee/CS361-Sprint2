# CS361-Sprint2
 Microservice for group work in OSU CS361
 This microservice will receive a request from the main program, generate a random quote from a .csv database, and send the quote back to the main program.

 The microservice leverages ZeroMQ for communication. More information about ZeroMQ can be found here: https://zeromq.org/languages/python/

 Here is an example on how to communicate with this microservice.

# ZeroMQ | Set-Up for main program
 Create the ZeroMQ context and socket for communication
 ```
 import zmq
 
 context = zmq.Context()
 socket = context.socket(zmq.REQ)
 socket.connect("tcp://localhost:5000")
 ```

# ZeroMQ | Send a request for quote
 The following code block will send a request to the microservice and assumes that the above code block is established.
 ```
 socket.send(b"Any message you want here")
 ```
 The message variable will be a Python string variable that is the quote.

# ZeroMQ | Receive a request for quote
 The following code block is how to receive the message and the quote.
 You must use "recv_string()" otherwise, you'll get a random byte attached to the quote.
 ```
 message = socket.recv_string()
 ```

# UML Diagram
![UML Diagram](https://github.com/kvn-lee/CS361-Sprint2/assets/32992749/cccaca27-8876-4223-99d9-405968803e4f)
