# Patient API
## About 
basic CRUD for manage data patient make with python

## CRUD database for:
- patients

## How to run app?
1. Clone this project to your local computer
2. make database name `hospital_zicare` or your choice name. if you user other name, change `sqlalchemy.url = mariadb://{username}:{password}@localhost:3306/{your name database}` at migration_db/alembic.ini 
3. run command `alembic upgrade heads` on migration_db
4. uncomment `create_patients()` in models.py migration_db, then run `python models.py`, now you have 5 data on database
5. Install required package alembic, fastapi, uvicorn, mysqlclient
6. run `uvicorn main:app --reload` in terminal at root folder

## Main EndPoint

| url        | Method           | Description  |
| ------------- |:-------------:| -----:|
| /patients      | GET | Get all data patients |
| /patients/{patient_id}      | GET | Get all data patient by id |
| /patient      | POST | Create patient |
| /patient      | PUT | Delete patient |
| /docs      | PUT | FastAPI - Swagger UI |

## source reference
- [Create API](https://www.youtube.com/watch?v=N8i4GcRRkV8&t=1169s) - Youtube
- [Migration DB](https://www.youtube.com/watch?v=nt5sSr1A_qw&t=825s) - Youtube