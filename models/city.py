#!/usr/bin/env python3
""" Module Defining the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class Definition

    Public class attrs:
        state_id -- The state id
        name -- The name of the city
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ The init constructor """
        super().__init__(*args, **kwargs)
