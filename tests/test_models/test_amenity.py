#!/usr/bin/env python3
"""
MOdule for unittests on amenity.py
"""
import uuid
import unittest
import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test Individual components for The amenity Model
    """
    def setUp(self):
        self.m = Amenity()

    # ++++++++++++++++++++++++++
    # start tests for attributes
    # ++++++++++++++++++++++++++

    def test_name(self):
        ''' Tests for name attribute.'''

        A = Amenity()
        # TAMEN-NM: test if name is a string object
        self.assertIs(type(A.name), str)

    def test_id(self):
        """
        Tests for id attribute of our amenity model
        """
        idd = self.m.id
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)

        # TAMEN-ID: test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # TAMEN-CA: Confirm that created_at exists
        self.assertNotEqual(self.m.created_at, None)

        # TAMEN-CA: test created_at is a datetime object
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # TAMEN-UA: test updated_at is not None object.
        self.assertNotEqual(self.m.updated_at, None)

        # TAMEN-UA: test updated_at is a datetime object.
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()

        # TAMEN-SV: test updated_at was updated on save.
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_dct = self.m.__dict__
        expected_dct.update(__class__="Amenity")

        # TAMEN-TD: test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), d.keys())

        # TAMEN-TD: test that to_dict returns type dict
        self.assertIs(type(d), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # TAMEN-ST: test that __str__() returns a string object
        self.assertIs(type(self.m.__str__()), str)
    # _________________________________________
    # end test for methods
    # ________________________________________
