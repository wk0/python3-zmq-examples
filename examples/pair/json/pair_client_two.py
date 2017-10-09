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
socket.connect("tcp://localhost:%s" % port)

print("I am the parent checking attendance!")

"""
Explicit encoding/decoding of unicode strings here,
can also do recv_string, send_string
"""
message_count = 0
while True:
    # Recieving Message
    msg = socket.recv_json()

    # Stops listening upon recieving end character
    if msg == -1:
        sys.exit(0)
    print(msg)


    # Preparing Message
    message_unicode = "Message #{} from school delivered!".format(message_count)
    message_utf8 = message_unicode.encode('utf-8')
    socket.send(message_utf8)
    message_count += 1

    time.sleep(1)
