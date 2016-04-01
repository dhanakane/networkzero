# -*- coding: utf-8 -*-
"""networkzero - easy network discovery & messaging

Aimed at a classrom or club situation, networkzero makes it simpler to
have several machines or several processes on one machine discovering
each other and talking across a network. Typical examples would include:

* Sending commands to a robot
* Sending scores to a scoreboard
* Having a remote sensor ping a central controller
* A peer-to-peer chat / instant messenger

Example code:

[Computer 1]:
import networkzero as nw0

echo_address = nw0.advertise("echo")
while True:
    name = nw0.wait_for_request(echo_address)
    nw0.send_reply(echo_address, "Hello " + name)

[Computer 2]:
import networkzero as nw0

echo_address = nw0.discover("echo")
print(nw0.send_request(echo_address, "Alice"))
print(nw0.send_request(echo_address, "Bob"))

"""

from .discovery import advertise, unadvertise, discover
from .messenger import (
    send_command, wait_for_command, 
    send_request, wait_for_request, send_reply, 
    publish_news, wait_for_news
)
from .core import address