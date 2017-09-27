#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
import struct
import encoding


class JsonEncoderTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 1}
        self.encoder = encoding.JsonEncoder()
        self.data = self.encoder.encode(self.obj)
        self.json_str = json.dumps(self.obj)

    def test_is_encoding(self):
        encoder = encoding.JsonEncoder()
        self.assertIsInstance(encoder, encoding.Encoder, msg=None)

    def test_encode(self):
        json_str = json.dumps(self.obj)
        raw_data = struct.pack('!I', len(json_str))
        raw_data += json_str
        self.assertEqual(raw_data, self.data, msg=None)

    def test_decode_no_enough(self):
        self.assertRaises(
            encoding.DataNoEnoughException,
            self.encoder.decode, '')
        self.assertRaises(
            encoding.DataNoEnoughException,
            self.encoder.decode,
            self.data[:3])
        self.assertRaises(
            encoding.DataNoEnoughException,
            self.encoder.decode,
            self.data[:4])

    def test_decode(self):
        self.assertDictEqual(
            self.obj,
            self.encoder.decode(self.data),
            msg=None)

    def test_complete(self):
        encoder = encoding.JsonEncoder()
        obj = {'a': 1}
        data = encoder.encode(obj)
        self.assertFalse(encoder.complete(''), msg=None)
        self.assertFalse(encoder.complete(data[:3]), msg=None)
        self.assertFalse(encoder.complete(data[:4]), msg=None)
        self.assertFalse(encoder.complete(data[:-1]), msg=None)
        self.assertTrue(encoder.complete(data), msg=None)
