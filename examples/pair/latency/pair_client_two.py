import zmq
import random
import sys
import time
from datetime import datetime

"""
Based on pair/simple within this project
* Sending datetime
* Measuring latency
"""

"""
Based on:
https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pair.html

Pair:
* The communication is bidirectional.
* There is no specific state stored within the socket
* There can only be one connected peer.
* The server listens on a certain port and a client connects to it.
"""
# Preset port, can use cmd line args
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

print("I am client two!")

for i in range(10):
    # Recieving Message
    msg_datetime = socket.recv_string()
    recieved_datetime = datetime.strptime(msg_datetime, "%Y-%m-%d %H:%M:%S.%f")
    assert(msg_datetime==str(recieved_datetime))

    # Calculate latency
    latency = datetime.now() - recieved_datetime
    print(str(latency))

    # Preparing Message
    message_datetime = str(datetime.now())
    socket.send_string(message_datetime)
