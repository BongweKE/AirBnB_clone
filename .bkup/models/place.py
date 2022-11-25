#!/usr/bin/python3
""" The city module.
"""
import uuid
import datetime
from models.base_model import BaseModel


class City(BaseModel):
    """ Implementation of the City class.
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_quest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
