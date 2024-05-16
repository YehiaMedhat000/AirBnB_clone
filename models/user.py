#!/usr/bin/env python3
""" Module for the User class definition """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class representing a user """

    def __init__(self, *args, **kwargs):
        """ Initialize a new User instance """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
