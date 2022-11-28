#!/usr/bin/env python3
"""
MOdule for unittests on user.py
"""
import uuid
import unittest
import datetime
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test Individual components for The User Model
    """
    def setUp(self):
        self.m = User()

    # Tests for attributes

    def test_email(self):
        ''' Tests for email attribute.'''

        # TUSER-EM: test if email is a string object
        self.assertIs(type(User.email), str)

    def test_password(self):
        ''' Tests for password attribute.'''

        # TUSER-PW: test if password is a string object
        self.assertIs(type(User.password), str)

    def test_first_name(self):
        ''' Tests for first_name attribute.'''

        # TUSER-FN: test if first_name is a string object
        self.assertIs(type(User.first_name), str)

    def test_last_name(self):
        ''' Tests for last_name attribute.'''

        # TUSER-LN: test if last_name is a string object
        self.assertIs(type(User.last_name), str)

    def test_id(self):
        """
        Tests for id attribute of our User model
        """
        idd = self.m.id
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)


        # TUSER-ID: test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # TUSER-CA: test that created at exists
        self.assertNotEqual(self.m.created_at, None)

        # TUSER-CA: test created_at is a datetime object
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # TUSER-UA: test updated_at is not None object.
        self.assertNotEqual(self.m.updated_at, None)

        # TUSER-UA: test updated_at is a datetime object.
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()

        # TUSER-SV: test updated_at was updated on save.
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_dct = self.m.__dict__
        expected_dct.update(__class__="User")

        # TUSER-TD: test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), d.keys())

        # TUSER-TD: test that to_dict returns type dict
        self.assertIs(type(d), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # TUSER-ST: test that __str__() returns a string object
        self.assertIs(type(self.m.__str__()), str)
    # _________________________________________
    # end test for methods
    # ________________________________________

    # to do for all:
    # - kwargs
    #
