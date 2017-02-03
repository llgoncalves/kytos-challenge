#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""kytos-challenge
A parser for a raw packet using the OpenFlow v.1.0 specification.

Copyright (C) 2017 Luan Luiz Gonçalves (luanlg.cco@gmail.com)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
import sys
from struct import unpack
import argparse


class OFTP(object):
    """Main class of kytos-challenge.

    The main responsabilities of this class are:
        - Get the header from raw packet (Only OFPT_HELLO packet);
        - Show the hearder information.
    """

    def __init__(self):
        """ Init method of OFTP."""
        self.__version = None
        self.__type = None
        self.__lenght = None
        self.__xid = None

    def parser(self, raw_packet):
        """Gets the header from raw packet.

        Header structure -- C Type:
            - Version: unsigned char (1 Byte);
            - Type: unsigned char (1 Byte);
            - Lenght: unsigned short (2 Bytes);
            - Xid:  unsigned int (4 Bytes).

        Note: Big-endian format.
        """
        self.__version = unpack('>B', raw_packet[0])[0]
        self.__type = unpack('>B', raw_packet[1:2])[0]
        self.__lenght = unpack('>H', raw_packet[2:4])[0]
        self.__xid = unpack('>I', raw_packet[4:8])[0]

    def show_header(self):
        """Print on stdout the hearder information."""
        sys.stdout.write("Version: " + str(self.__version) + "\n" +
                         "Type: " + str(self.__type) + "\n" +
                         "Lenght: " + str(self.__lenght) + "\n" +
                         "Xid: " + str(self.__xid) + "\n")


def main(file_name):
    """ Reads the raw packet from the binary file and use the class OFTP to
        get and show the packet hearder."""
    try:
        bin_file = open(file_name, "rb")
        raw_packet = bin_file.read()
        bin_file.close()
    except IOError:
        sys.stdout.write("File doesn't exist!\n")
        exit()

    oftp = OFTP()
    oftp.parser(raw_packet)
    oftp.show_header()

if __name__ == '__main__':
    """Parses the arguments and call the main method."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default=["ofpt_hello.dat"], nargs=1, type=str,
                        help="Input file name")
    args = parser.parse_args()
    file_name = args.f[0]
    main(file_name)
