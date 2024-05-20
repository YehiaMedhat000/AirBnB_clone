#!/usr/bin/env python3
""" Module Defining the Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class Definition

    Public class attrs:
        state_id -- The state id
        name -- The name of the city
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """ The init constructor """
        super().__init__(*args, **kwargs)
