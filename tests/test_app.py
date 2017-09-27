#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from encoding.encoding import Encoder
from saf import app
from saf.exceptions import EncoderTypeException, CallbackTypeException


def process(req, rsp):
    pass


class AppTestCase(unittest.TestCase):
    def test_run(self):
        a = app.App('0.0.0.0', 8080, None, None, 0, 0)
        self.assertEqual(1, a.worker_size(), msg=None)
        self.assertEqual(1, a.queue_size(), msg=None)

    def test_callback_type_exception(self):
        a = app.App('0.0.0.0', 8080, None, None, 0, 0)
        self.assertRaises(CallbackTypeException, callableObj=a.run)

    def test_encoder_type_exception(self):
        def callback():
            pass
        a = app.App('0.0.0.0', 8080, callback, None, 0, 0)
        self.assertRaises(EncoderTypeException, callableObj=a.run)

        class Encoder(object):
            pass
        b = app.App('0.0.0.0', 8080, callback, Encoder(), 0, 0)
        self.assertRaises(EncoderTypeException, callableObj=b.run)

    def test_no_exception(self):
        def callback():
            pass

        class TestEncoder(Encoder):
            pass
        a = app.App('0.0.0.0', 8080, callback, TestEncoder(), 0, 0)
        a.run()


if __name__ == '__main__':
    unittest.main()
