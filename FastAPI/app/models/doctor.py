"""
This module contains the Doctor model.
"""

from pydantic import BaseModel

class Doctor(BaseModel):
    """
    Doctor model representing a doctor with an id, name, and specialty.
    """
    id: int
    name: str
    specialty: str
