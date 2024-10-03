"""
This module establishes a connection to a MySQL database 
using Peewee ORM and environment variables.
"""

import os
from dotenv import load_dotenv
from peewee import MySQLDatabase, Model, AutoField, CharField, ForeignKeyField, DateField

# Load environment variables from the .env file
load_dotenv()

# Create a MySQL database instance using environment variables
DATABASE = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),

)

# pylint: disable=too-few-public-methods
class DoctorModel(Model):
    """Represents a doctor with attributes such as name and specialty."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    specialty = CharField(max_length=100)

    class Meta:
        """Meta information for the DoctorModel."""
        database = DATABASE
        table_name = "doctors"


# pylint: disable=too-few-public-methods
class PatientModel(Model):
    """Represents a patient with attributes such as name, date of birth, and doctor (doctor_id)."""

    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    date_of_birth = DateField()
    doctor_id = ForeignKeyField(DoctorModel, backref="patients")

    class Meta:
        """Meta information for the PatientModel."""
        database = DATABASE
        table_name = "patients"
