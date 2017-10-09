import sys
import zmq

"""
Based on:
http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.htmlPair:

Pub/Sub:
Senders of messages, called publishers, do not program the messages to be sent
directly to specific receivers, called subscribers. Messages are published
without the knowledge of what or if any subscriber of that knowledge exists.
"""

port = "5557"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:%s" % port)

# Subscribe to zipcode, default is NYC, 10001
# NOTE: For some reason, I can't get it working without a topic filter
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
for i in range (5):
    string = socket.recv_string()
    topic, messagedata = string.split()
    print(topic, messagedata)
