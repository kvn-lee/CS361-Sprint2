import zmq
import csv
import random

# Create context
context = zmq.Context()

# Create socket
socket = context.socket(zmq.REP)

# Bind socket to main program
socket.bind("tcp://localhost:5000")


def GenerateQuote():
    """
    Function will generate a motivational quote
    .csv file exists with a database of quotes to use
    """

    filename = "quotes.csv"
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)

    return rows[random.randint(1, len(rows)-1)][1]


while True:
    request = socket.recv()
    print("Received request: %s" % request)

    quote = GenerateQuote()
    print(quote)

    socket.send_string(quote)
    print("Request sent")
