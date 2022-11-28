#!/usr/bin/env python3
"""
MOdule for unittests on base_model.py
"""
import uuid
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
        idd = self.m.id
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)


        # TBASE-ID: test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # TBASE-CA
        self.assertNotEqual(self.m.created_at, None)

        # TBASE-CA: test created_at is a datetime object
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # TBASE-UA: test updated_at is not None object.
        self.assertNotEqual(self.m.updated_at, None)

        # TBASE-UA: test updated_at is a datetime object.
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()

        # TBASE-SV: test updated_at was updated on save.
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_dct = self.m.__dict__
        expected_dct.update(__class__="BaseModel")

        # TBASE-TD: test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), d.keys())

        # TBASE-TD: test that to_dict returns type dict
        self.assertIs(type(d), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # TBASE-ST: test that __str__() returns a string object
        self.assertIs(type(self.m.__str__()), str)

        # TBASE-ST: test that __str__ returns a string for the right class
        self.assertEqual(self.m.__str__().split()[0], "[BaseModel]")
    # _________________________________________
    # end test for methods
    # ________________________________________
