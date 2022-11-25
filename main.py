from model import PatientTable, Patient
from db import session, ENGINE
from fastapi import FastAPI
from datetime import datetime
from typing import List
import model

model.Base.metadata.create_all(bind=ENGINE)

app = FastAPI()


@app.get('/')
def start():
    return {'server': 'running succesfully'}


@app.get('/patients', description='get all patient')
def read_patients():
    patients = session.query(PatientTable).all()
    return patients


@app.get('/patients/{patient_id}', description='get patient by id')
def read_patient(patient_id: int):
    patient = session.query(PatientTable).filter(
        PatientTable.id == patient_id).first()
    return patient


@app.post('/patient', description='create patient')
def create_patients(first_name: str, last_name: str, birth: datetime):
    patient = PatientTable()
    patient.first_name = first_name
    patient.last_name = last_name
    patient.birth = birth

    session.add(patient)
    session.commit()

    return f'{first_name} {last_name} createed...'


@app.put('/patients', description='update patient')
def update_patients(patients: List[Patient]):

    for i in patients:
        patient = session.query(PatientTable).filter(
            PatientTable.id == i.id).first()
        patient.first_name = i.first_name
        patient.last_name = i.last_name
        patient.birth = i.birth
        session.commit()

    return f'{patients[0].first_name} {patients[0].last_name} updated...'


@app.delete('/patient', description='delete patient')
def delete_patients(patient_id: int):
    patient = session.query(PatientTable).filter(
        PatientTable.id == patient_id).delete()
    session.commit()

    return f'delete successfully...'
