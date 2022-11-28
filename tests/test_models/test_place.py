#!/usr/bin/env python3
"""
MOdule for unittests on place.py
"""
import uuid
import unittest
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test Individual components for The place Model
    """
    def setUp(self):
        self.m = Place()

    # ++++++++++++++++++++++++++
    # start tests for attributes
    # ++++++++++++++++++++++++++

    def test_city_id(self):
        ''' Tests for city_id attribute.'''

        # TPLAC-CI: test if city_id is a string object
        self.assertIs(type(Place.city_id), str)

    def test_user_id(self):
        ''' Tests for user_id attribute.'''

        # TPLAC-UI: test if city_id is a string object
        self.assertIs(type(Place.user_id), str)

    def test_name(self):
        ''' Tests for name attribute.'''

        # TPLAC-NM: test if name is a string object
        self.assertIs(type(Place.name), str)

    def test_description(self):
        ''' Tests for description attribute.'''

        # TPLAC-DS: test if description is a string object
        self.assertIs(type(Place.description), str)

    def test_number_rooms(self):
        ''' Tests for number_rooms attribute.'''

        # TPLAC-NR: test if name is an int object
        self.assertIs(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        ''' Tests for number_bathrooms attribute.'''

        # TPLAC-NB: test if number_bathrooms is an int object
        self.assertIs(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        ''' Tests for max_guest attribute.'''

        # TPLAC-MG: test if max_guest is an int object
        self.assertIs(type(Place.max_guest), int)

    def test_price_by_night(self):
        ''' Tests for price_by_night attribute.'''

        # TPLAC-PN: test if price_by_night is an int object
        self.assertIs(type(Place.price_by_night), int)

    def test_latitude(self):
        ''' Tests for latitude attribute.'''

        # TPLAC-LA: test if latitude is a float object
        self.assertIs(type(Place.latitude), float)

    def test_longitude(self):
        ''' Tests for longitude attribute.'''

        # TPLAC-LO: test if longitude is a float object
        self.assertIs(type(Place.longitude), float)

    def test_amenity_ids(self):
        ''' Tests for amenity_ids attribute.'''

        # TPLAC-AI: test if amenity_ids is a list object
        self.assertIs(type(Place.amenity_ids), list)

    def test_id(self):
        """
        Tests for id attribute of our place model
        """
        idd = self.m.id
        self.assertNotEqual(self.m.id, None)
        self.assertIs(type(self.m.id), str)


        # TPLAC-ID: test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # TPLAC-CA: confirm created_at exists
        self.assertNotEqual(self.m.created_at, None)

        # TPLAC-CA: test created_at is a datetime object
        self.assertIs(type(self.m.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # TPLAC-UA: test updated_at is not None object.
        self.assertNotEqual(self.m.updated_at, None)

        # TPLAC-UA: test updated_at is a datetime object.
        self.assertIs(type(self.m.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.m.updated_at
        self.m.save()

        # TPLAC-SV: test updated_at was updated on save.
        self.assertNotEqual(self.m.updated_at, prev_updated_at)

    def test_to_dict(self):
        d = self.m.to_dict()
        expected_dct = self.m.__dict__
        expected_dct.update(__class__="Place")

        # TPLAC-TD: test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), d.keys())

        # TPLAC-TD: test that to_dict returns type dict
        self.assertIs(type(d), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # TPLAC-ST: test that __str__() returns a string object
        self.assertIs(type(self.m.__str__()), str)
    # _________________________________________
    # end test for methods
    # ________________________________________
