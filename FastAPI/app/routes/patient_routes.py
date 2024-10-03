# app/patient_routes.py

"""
Module that defines the routes for managing patients.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting patients through a REST API.

Available routes:

- POST /patients/: Creates a new patient.
- GET /patients/{patient_id}: Retrieves patient information by ID.
- PUT /patients/{patient_id}: Updates patient information.
- DELETE /patients/{patient_id}: Deletes a patient.

Each route uses the `PatientService` to interact with the
business logic related to patients.
"""

from app.services.patient_service import PatientService
from app.models.patient import Patient
from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/patients",
    tags=["patients"],
)


@router.post("/patients/", response_model=Patient)
def create_patient(name: str, date_of_birth: str, doctor_id: int) -> Patient:
    """
    Create a new patient.

    Args:
        name (str): The name of the patient.
        date_of_birth (str): The birthdate of the patient.
        doctor_id (int): The ID of the assigned doctor.

    Returns:
        Patient: The created patient instance.
    """
    patient = PatientService.create_patient(name, date_of_birth, doctor_id)
    return patient


@router.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int) -> Patient:
    """
    Retrieve patient information by ID.

    Args:
        patient_id (int): The ID of the patient to retrieve.

    Returns:
        Patient: The patient with the specified ID.

    Raises:
        HTTPException: If the patient is not found.
    """
    patient = PatientService.get_patient_by_id(patient_id)
    if patient:
        return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@router.put("/patients/{patient_id}", response_model=Patient)
def update_patient(
    patient_id: int, name: str = None, date_of_birth: str = None, doctor_id: int = None
) -> Patient:
    """
    Update patient information.

    Args:
        patient_id (int): The ID of the patient to update.
        name (str, optional): The new name of the patient.
        date_of_birth (str, optional): The new birthdate of the patient.
        doctor_id (int, optional): The new doctor's ID.

    Returns:
        Patient: The updated patient instance.

    Raises:
        HTTPException: If the patient is not found.
    """
    patient = PatientService.update_patient(patient_id, name, date_of_birth, doctor_id)
    if patient:
        return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@router.delete("/patients/{patient_id}")
def delete_patient(patient_id: int) -> dict:
    """
    Delete a patient by ID.

    Args:
        patient_id (int): The ID of the patient to delete.

    Returns:
        dict: A confirmation message if the patient was deleted.

    Raises:
        HTTPException: If the patient is not found.
    """
    if PatientService.delete_patient(patient_id):
        return {"message": "Patient deleted successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")
