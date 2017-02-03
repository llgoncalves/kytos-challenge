# kytos-challenge

##Problem Statement

The OpenFlow is a network protocol used to define how the communication between Network Switches and hosts will happen. This protocol is implemented using a traditional client/server architecture.

The `file ofpt_hello.dat` available in this repository contain one raw packet collected from tcpdump. This packet contains a message from an OpenFlow switch (server) to our OpenFlow controller (client).

Your task is to write a parser for this raw packet using the OpenFlow v.1.0 specification. You must print on stdout the maximum amount of information that you can.

This is a binary file with only one message: a `OFPT_HELLO` packet.

You can use Google or any another resource to finish this task, also please refer to the [OpenFlow 1.0 Specification](http://archive.openflow.org/documents/openflow-spec-v1.0.0.pdf).

* Page 2: Specs about open flow headers;
* Page 41: Specs about `OFPT_HELLO` messages.

##Running
    python parser.py

##Help
Usage: `parser.py [-h] [-f F]`

Optional arguments:

    -h, --help  show this help message and exit
    -f F        Input file name 
    
Default input file name: `ofpt_hello.dat`

