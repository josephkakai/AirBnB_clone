#!/usr/bin/python3
"""User inheriting from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """class user inheriting from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
