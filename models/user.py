#!/usr/bin/echo python3
"""class user inheriting from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """class user inherintimg from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
