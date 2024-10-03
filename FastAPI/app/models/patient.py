"""
This module contains the Patient model.
"""

from pydantic import BaseModel

class Patient(BaseModel):
    """
    Patient model representing a patient with an id, name, birth date, and doctor_id.
    """
    id: int
    name: str
    date_born: str
    doctor_id: int
