# app/doctor_routes.py

"""
Module that defines the routes for managing doctors.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting doctors through a REST API.

Available routes:

- POST /doctors/: Creates a new doctor.
- GET /doctors/{doctor_id}: Retrieves doctor information by ID.
- PUT /doctors/{doctor_id}: Updates doctor information.
- DELETE /doctors/{doctor_id}: Deletes a doctor.

Each route uses the `DoctorService` to interact with the
business logic related to doctors.
"""

from app.services.doctor_service import DoctorService  # pylint: disable=import-error
from app.models.doctor import Doctor
from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
)



@router.post("/doctors/", response_model=Doctor)
def create_doctor(name: str, specialty: str) -> Doctor:
    """
    Create a new doctor.

    Args:
        name (str): The name of the doctor.
        specialty (str): The specialty of the doctor.

    Returns:
        Doctor: The created doctor.
    """
    doctor = DoctorService.create_doctor(name, specialty)
    return doctor


@router.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int) -> Doctor:
    """
    Retrieve doctor information by ID.

    Args:
        doctor_id (int): The ID of the doctor to retrieve.

    Returns:
        Doctor: The doctor with the specified ID.

    Raises:
        HTTPException: If the doctor is not found.
    """
    doctor = DoctorService.get_doctor_by_id(doctor_id)
    if doctor:
        return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")


@router.put("/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, name: str = None, specialty: str = None) -> Doctor:
    """
    Update doctor information.

    Args:
        doctor_id (int): The ID of the doctor to update.
        name (str, optional): The new name of the doctor.
        specialty (str, optional): The new specialty of the doctor.

    Returns:
        Doctor: The updated doctor.

    Raises:
        HTTPException: If the doctor is not found.
    """
    doctor = DoctorService.update_doctor(doctor_id, name, specialty)
    if doctor:
        return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")


@router.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int) -> dict:
    """
    Delete a doctor by ID.

    Args:
        doctor_id (int): The ID of the doctor to delete.

    Returns:
        dict: A confirmation message if the doctor was deleted.

    Raises:
        HTTPException: If the doctor is not found.
    """
    if DoctorService.delete_doctor(doctor_id):
        return {"message": "Doctor deleted successfully"}
    raise HTTPException(status_code=404, detail="Doctor not found")
