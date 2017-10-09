import zmq
import random
import sys
import time

"""
Based on pair/simple within this project
* Sending json
* incorporating message loop with a function
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

print("Client One: School attendance broadcaster")
students = ['James', 'Maria', 'Zoe', 'Chris', 'Angela']
monday    = {'present': students,
             'absent' : []}
tuesday   = {'present': ['James', 'Maria', 'Zoe', 'Chris'],
             'absent' : ['Angela']}
wednesday = {'present': ['Maria', 'Zoe', 'Angela'],
             'absent' : ['James', 'Chris']}
thursday  = {'present': ['James', 'Maria', 'Zoe', 'Chris'],
             'absent' : ['Angela']}
friday    = {'present': [],
             'absent' : students}

# -1 is to indicate end of message
week = [monday, tuesday, wednesday, thursday, friday, -1]

"""
Explicit encoding/decoding of unicode strings here,
can also do recv_string, send_string
"""
message_count = 0
for day in week:
    # Preparing Message
    socket.send_json(day)
    message_count += 1

    # Exit after sending -1 final message,
    #   otherwise hangs waiting to recieve
    if day == -1:
        sys.exit(1)

    # Recieving Message
    msg = socket.recv()
    msg_unicode = msg.decode("utf-8")
    print(msg_unicode)

    time.sleep(1)
