#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Encoder(object):

    """The base class for all encoder"""

    def __init__(self):
        """TODO: to be defined1. """

    def encode(self, msg):
        """encode msg to network buffer

        :returns: encoded buffer

        """
        raise NotImplementedError

    def decode(self, buf):
        """decode buf to msg

        :returns: msg

        """
        raise NotImplementedError
