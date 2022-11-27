#!/usr/bin/env python3
"""
MOdule for unittests on city.py
"""
import uuid
import unittest
import datetime
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test Individual components for The city Model
    """
    def setUp(self):
        self.m = City()

    # Tests for attributes
    def test_id(self):
        """
        Tests for id attribute of our city model
        """
        idd = self.m.id
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)

        # TCITY-ID: test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # TCITY-CA: confirm that created at exists
        self.assertNotEqual(self.m.created_at, None)

        # TCITY-CA: test created_at is a datetime object
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # TCITY-UA: test updated_at is not None object.
        self.assertNotEqual(self.m.updated_at, None)

        # TCITY-UA: test updated_at is a datetime object.
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()

        # TCITY-SV: test updated_at was updated on save.
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_dct = self.m.__dict__
        expected_dct.update(__class__="City")

        # TCITY-TD: test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), d.keys())

        # TCITY-TD: test that to_dict returns type dict
        self.assertIs(type(d), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # TCITY-ST: test that __str__() returns a string object
        self.assertIs(type(self.m.__str__()), str)
    # _________________________________________
    # end test for methods
    # ________________________________________
