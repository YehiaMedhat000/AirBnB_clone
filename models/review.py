#!/usr/bin/env python3
""" Module defining the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class definition

    Public class attrs:
        place_id -- The id of the place reviewed
        user_id -- The id of the user reviewing
        text -- The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
