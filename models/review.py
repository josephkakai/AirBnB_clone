<<<<<<< HEAD
#!/usr/bin/env python3
"""class review inheriting from BaseModel"""

=======
#!/usr/bin/python3
"""Defines the Review class."""
>>>>>>> main
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """class review inheriting from baseModel
=======
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
>>>>>>> main
    """

    place_id = ""
    user_id = ""
    text = ""
