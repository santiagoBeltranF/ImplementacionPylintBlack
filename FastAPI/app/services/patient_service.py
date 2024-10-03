"""
Service layer for Patient operations.

This module contains the business logic for managing patients.
It interacts with the `PatientModel` from the database and uses
the `Patient` Pydantic model for data validation.
"""

from typing import Optional
from peewee import DoesNotExist
from app.database import PatientModel, DoctorModel
from app.models.patient import Patient


class PatientService:
    """Service layer for Patient operations"""

    @staticmethod
    def create_patient(name: str, date_of_birth: str, doctor_id: int) -> Patient:
        """
        Create a new patient.

        Args:
            name (str): The name of the patient.
            date_of_birth (str): The birthdate of the patient.
            doctor_id (int): The ID of the assigned doctor.

        Returns:
            Patient: The created patient instance.

        Raises:
            ValueError: If the doctor with the given ID does not exist.
        """
        try:
            doctor_instance = DoctorModel.get_by_id(doctor_id)
            patient_instance = PatientModel.create(
                name=name, date_of_birth=date_of_birth, doctor_id=doctor_instance
            )
            # Using from_orm to convert Peewee model to Pydantic model
            return Patient.from_orm(patient_instance)
        except DoesNotExist as exc:
            raise ValueError(f"Doctor with id {doctor_id} not found") from exc

    @staticmethod
    def get_patient_by_id(patient_id: int) -> Optional[Patient]:
        """
        Retrieve a patient by ID.

        Args:
            patient_id (int): The ID of the patient to retrieve.

        Returns:
            Optional[Patient]: The patient instance if found, else None.
        """
        try:
            patient_instance = PatientModel.get_by_id(patient_id)
            # Using from_orm to convert Peewee model to Pydantic model
            return Patient.from_orm(patient_instance)
        except DoesNotExist:
            return None

    @staticmethod
    def update_patient(
        patient_id: int,
        name: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        doctor_id: Optional[int] = None,
    ) -> Optional[Patient]:
        """
        Update an existing patient by ID.

        Args:
            patient_id (int): The ID of the patient to update.
            name (Optional[str]): The new name of the patient.
            date_of_birth (Optional[str]): The new birthdate of the patient.
            doctor_id (Optional[int]): The new doctor's ID.

        Returns:
            Optional[Patient]: The updated patient instance if successful, else None.

        Raises:
            ValueError: If the doctor with the given ID does not exist.
        """
        try:
            patient_instance = PatientModel.get_by_id(patient_id)

            # Update fields only if new values are provided
            if name:
                patient_instance.name = name
            if date_of_birth:
                patient_instance.date_of_birth = date_of_birth
            if doctor_id:
                try:
                    doctor_instance = DoctorModel.get_by_id(doctor_id)
                    patient_instance.doctor_id = doctor_instance
                except DoesNotExist as exc:
                    raise ValueError(f"Doctor with id {doctor_id} not found") from exc

            patient_instance.save()
            return Patient.from_orm(patient_instance)

        except DoesNotExist:
            return None

    @staticmethod
    def delete_patient(patient_id: int) -> bool:
        """
        Delete a patient by ID.

        Args:
            patient_id (int): The ID of the patient to delete.

        Returns:
            bool: True if the patient was deleted, else False.
        """
        try:
            # Check if the patient exists before attempting to delete
            patient_instance = PatientModel.get_by_id(patient_id)
            patient_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
