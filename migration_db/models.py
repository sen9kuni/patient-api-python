from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

# class untuk membuat tabel di database


class patientModel(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(225), nullable=False)
    last_name = Column(String(225), nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)
# class untuk membuat tabel di database
# sampai sini command
# 'alembic revision --autogenerate -m "{pesan yang akan di tinggalkan}"' di terminal untuk membuat/generate file migrate ke database
# lalu command 'alembic upgrade heads' dan database akan membuat table patient
# note: saya menemukan error yang mengharuskan saya untuk meng install mysqlclient, jadi saya run comand 'pip install mysqlclient' pada terminal


# mebuat data yang akan di input ke database
patients = [
    patientModel(first_name='Bob', last_name='pressto',
                 birth=datetime(1990, 6, 10)),
    patientModel(first_name='foo', last_name='dems',
                 birth=datetime(1997, 9, 9)),
    patientModel(first_name='saco', last_name='rams',
                 birth=datetime(1980, 6, 7)),
    patientModel(first_name='bud', last_name='liter',
                 birth=datetime(1992, 1, 1)),
    patientModel(first_name='woody', last_name='cowgirl',
                 birth=datetime(1999, 9, 8)),
]

# untuk mengkonesikan database
session_maker = sessionmaker(bind=create_engine(
    'mariadb://root:@localhost:3306/hospital_zicare'))

# function untuk menambah data ke tabel patient


def create_patients():
    with session_maker() as session:
        for patient in patients:
            session.add(patient)
        session.commit()

# memanggil function via terminal python models.py
# create_patients()
