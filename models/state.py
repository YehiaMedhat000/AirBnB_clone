#!/usr/bin/env python3
""" Module defining the State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class definition of the

    Public class attrs:
        name -- The name of the state
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """ The init constructor """
        super().__init__(*args, **kwargs)
