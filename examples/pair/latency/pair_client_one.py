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
socket.bind("tcp://*:%s" % port)

print("I am client one!")

"""
recv_string(), send_string()

These methods simply wrap their bytes counterpart by encoding to/decoding
from bytes around them, andThese methods simply wrap their bytes counterpart
by encoding to/decoding from bytes around them, and they all take an encoding
keyword argument that defaults to utf-8 they all take an encoding keyword
argument that defaults to utf-8
"""
for i in range(10):
    # Preparing Message
    message_datetime = str(datetime.now())
    socket.send_string(message_datetime)

    # Recieving Message
    msg_datetime = socket.recv_string()
    recieved_datetime = datetime.strptime(msg_datetime, "%Y-%m-%d %H:%M:%S.%f")
    assert(msg_datetime==str(recieved_datetime))

    # Calculate latency
    latency = datetime.now() - recieved_datetime
    print(str(latency))
