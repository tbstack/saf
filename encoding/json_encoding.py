#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct
import json
import encoding


class JsonEncoder(encoding.Encoder):

    """encode/decode json"""

    def __init__(self):
        """TODO: to be defined1. """
        self.__header_size = struct.calcsize('!I')

    def encode(self, obj):
        """encode obj to json data

        :returns: str

        """
        json_str = json.dumps(obj).encode()
        data = struct.pack('!I', len(json_str))
        data += json_str
        return data

    def decode(self, data):
        """decode data to obj

        :returns: dict

        """
        if not self.complete(data):
            raise encoding.DataNoEnoughException
        return json.loads(data[self.__header_size:].decode())

    def complete(self, data):
        """check data completed or not

        :returns: True if completed

        """
        data_len = len(data)
        if data_len < self.__header_size:
            return False
        header = self.__header(data)
        if data_len < header[0] + self.__header_size:
            return False
        return True

    def __header(self, data):
        return struct.unpack('!I', data[:self.__header_size])
