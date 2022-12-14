#!/usr/bin/env python3
"""
MOdule for unittests on base_model.py
"""
import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test Individual components for The base Model
    """
    def setUp(self):
        self.m = BaseModel()

    # Tests for attributes
    def test_id(self):
        """
        Tests for id attribute of our base model
        """
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)

    def test_created_at(self):
        self.assertNotEqual(self.m.created_at, None)
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        self.assertNotEqual(self.m.updated_at, None)
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_keys = self.__dict__.keys()
        expexted_keys.update(__class__=self.__class__.__name__)
        expected_attrs = list(expected_keys.keys())
        current_keys = list(d.keys())
        self.assertSetEqual(set(expected_keys), set(current_keys))
        self.assertEqual(d['__class__'], expected_keys["__class"])
        self.assertIs(type(d), dict)

    def test_str(self):
        self.assertIs(type(self.m.__str__), str)
    # _________________________________________
    # end test for methods
    # ________________________________________
