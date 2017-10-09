import zmq
import random
import sys
import time

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
Explicit encoding/decoding of unicode strings here,
can also do recv_string, send_string
"""
message_count = 0
while True:
    # Preparing Message
    message_unicode = "Message #{} from client one.".format(message_count)
    message_utf8 = message_unicode.encode('utf-8')
    socket.send(message_utf8)
    message_count += 1

    # Recieving Message
    msg = socket.recv()
    msg_unicode = msg.decode("utf-8")
    print(msg_unicode)

    time.sleep(1)
