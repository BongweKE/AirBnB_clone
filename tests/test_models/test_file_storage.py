#!/usr/bin/env python3
""" Test module for FileStorage class.
"""
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest


class TestFileStorage(unittest.TestCase):
    """ TestCase implementation for FileStorage class
    """
    # -----------------------
    # start tests for methods
    # -----------------------

    def setUp(self):
        ''' Sets up the environment for each test method.'''
        B = BaseModel()
        U = User()

    def test_all(self):
        ''' Tests the all method.'''
        types = [int, float, str, list, tuple, set, None]

        # TFILE-AL: test that all() returns an object of only one type - dict
        for cls in types:
            with self.subTest(i=cls):
                self.assertIsNot(type(storage.all()), cls)

    def test_new(self):
        ''' Tests the new method.'''
        classes = [BaseModel, User, Place, State, City, Amenity, Review]

        # TFILE-NW: test that new() adds new instances of all clss to __object
        for cls in classes:
            prev_objs = storage.all().copy()  # new dict obj; not ref to prev
            cls()  # create new instance of cls; should be added by new()
            curr_objs = storage.all()
            with self.subTest(i=cls):
                self.assertNotEqual(prev_objs, curr_objs)  # if new obj added

    def test_save(self):
        ''' Tests the save() method.'''
        storage.save()
        storage.reload()
        old_storage = storage.all().copy()  # collect present __objects
# --------------------------------------------
        storage.save()
        storage.reload()
        newish_storage = storage.all().copy()

        # TFILE-SV: test that no change in storage when no new instance creatd
        self.assertEqual(old_storage.keys(), newish_storage.keys())
# -------------------------------------------
        Place(), State()  # create two new instances added to __objects autom.
        storage.save()  # save __objects with newly added instances
        storage.reload()
        new_storage = storage.all()

        # TFILE-SV: test that current __objects is actually saved to file.
        self.assertNotEqual(old_storage, new_storage)

        # TFILE-SV: test that save() returns None
        self.assertIs(storage.save(), None)
    # ------------------------
    # end of tests for methods
    # ------------------------

    # ++++++++++++++++++++++++++
    # start tests for attributes
    # ++++++++++++++++++++++++++

    def test_objects(self):
        ''' Tests the __objects attribute.'''

        # TFILE-OB: test that type of __object is dict
        self.assertIs(type(storage.all()), dict)
    # +++++++++++++++++++++++
    # end test for attributes
    # +++++++++++++++++++++++
