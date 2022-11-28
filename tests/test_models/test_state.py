#!/usr/bin/env python3
"""
MOdule for unittests on state.py
"""
import uuid
import unittest
import datetime
from models.state import State

class TestState(unittest.TestCase):
    """
    Test Individual components for The state Model
    """
    def setUp(self):
        self.m = State()

    # Tests for attributes

    def test_name(self):
        ''' Tests for name attribute.'''

        # TSTAT-NM: test if name is a string object
        self.assertIs(type(State.name), str)

    def test_id(self):
        """
        Tests for id attribute of our state model
        """
        idd = self.m.id
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)


        # TSTAT-ID: test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # TSTAT-CA: test that create_at exists
        self.assertNotEqual(self.m.created_at, None)

        # TSTAT-CA: test created_at is a datetime object
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # TSTAT-UA: test updated_at is not None object.
        self.assertNotEqual(self.m.updated_at, None)

        # TSTAT-UA: test updated_at is a datetime object.
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()

        # TSTAT-SV: test updated_at was updated on save.
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_dct = self.m.__dict__
        expected_dct.update(__class__="State")

        # TSTAT-TD: test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), d.keys())

        # TSTAT-TD: test that to_dict returns type dict
        self.assertIs(type(d), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # TSTAT-ST: test that __str__() returns a string object
        self.assertIs(type(self.m.__str__()), str)
    # _________________________________________
    # end test for methods
    # ________________________________________
