#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from socket import socket, AF_INET, SOCK_STREAM
# from threading import Thread
# from queue import Queue
from .exceptions import EncoderTypeException, CallbackTypeException
from encoding.encoding import Encoder


class App(object):
    """server app"""

    def __init__(self, addr, port, callback, encoder, workersize, queuesize):
        """TODO: to be defined1. """
        self.__addr = addr
        self.__port = port
        self.__callback = callback
        self.__encoder = encoder
        self.__workersize = workersize if workersize > 0 else 1
        self.__queuesize = queuesize if queuesize > 0 else 1

    def run(self):
        """run and serve

        :returns: True if success

        """
        if not callable(self.__callback):
            raise CallbackTypeException
        if not isinstance(self.__encoder, Encoder):
            raise EncoderTypeException

    def worker_size(self):
        return self.__workersize

    def queue_size(self):
        return self.__queuesize
