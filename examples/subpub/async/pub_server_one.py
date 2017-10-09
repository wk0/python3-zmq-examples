import zmq
import random
import sys
import time

"""
Based on:
http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.htmlPair:

Pub/Sub:
Senders of messages, called publishers, do not program the messages to be sent
directly to specific receivers, called subscribers. Messages are published
without the knowledge of what or if any subscriber of that knowledge exists.
"""

port = "5555"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    topic = 88888
    messagedata = random.randrange(1,215) - 80
    print("%d %d" % (topic, messagedata))
    socket.send_string("%d %d" % (topic, messagedata))
    time.sleep(1)
