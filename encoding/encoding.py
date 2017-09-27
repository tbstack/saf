#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DataNoEnoughException(Exception):
    def __init__(self):
        super(DataNoEnoughException, self).__init__()


class Encoder(object):

    """The base class for all encoder"""

    def __init__(self):
        """TODO: to be defined1. """

    def encode(self, obj):
        """encode obj to network buffer

        :returns: encoded buffer

        """
        raise NotImplementedError

    def decode(self, data):
        """decode data to obj

        :returns: obj

        """
        raise NotImplementedError

    def complete(self, data):
        """check the receive buffer is completed or not.
        Only use by tcp.

        :returns: True if completed.

        """
        raise NotImplementedError
