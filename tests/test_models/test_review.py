#!/usr/bin/env python3
"""
MOdule for unittests on review.py
"""
import uuid
import unittest
import datetime
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Test Individual components for The review Model
    """
    def setUp(self):
        self.m = Review()

    # Tests for attributes

    def test_place_id(self):
        ''' Tests for place_id attribute.'''

        # TREVI-PI: test if place_id is a string object
        self.assertIs(type(Review.place_id), str)

    def test_user_id(self):
        ''' Tests for user_id attribute.'''

        # TREVI-UI: test if user_id is a string object
        self.assertIs(type(Review.user_id), str)

    def test_text(self):
        ''' Tests for text attribute.'''

        # TREVI-TX: test if text is a string object
        self.assertIs(type(Review.text), str)

    def test_id(self):
        """
        Tests for id attribute of our review model
        """
        idd = self.m.id
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)


        # TREVI-ID: test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # TREVI-CA: enure created_at exists
        self.assertNotEqual(self.m.created_at, None)

        # TREVI-CA: test created_at is a datetime object
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # TREVI-UA: test updated_at is not None object.
        self.assertNotEqual(self.m.updated_at, None)

        # TREVI-UA: test updated_at is a datetime object.
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()

        # TREVI-SV: test updated_at was updated on save.
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_dct = self.m.__dict__
        expected_dct.update(__class__="Review")

        # TREVI-TD: test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), d.keys())

        # TREVI-TD: test that to_dict returns type dict
        self.assertIs(type(d), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # TREVI-ST: test that __str__() returns a string object
        self.assertIs(type(self.m.__str__()), str)
    # _________________________________________
    # end test for methods
    # ________________________________________
