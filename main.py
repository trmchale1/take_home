from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import urllib

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'demo')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'demouser')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'password123')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username,db_password, host_server, db_server_port, database_name, ssl_mode)

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

store = sqlalchemy.Table(
    "store",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
metadata.create_all(engine)

class StoreIn(BaseModel):
    name: str

class Stores(BaseModel):
    id: int
    name: str

app = FastAPI(title = "Take home test")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/store/", response_model=Stores, status_code = status.HTTP_201_CREATED)
async def create_store(store: StoreIn):
    query = store.insert().values(name=Stores.name)
    last_record_id = await database.execute(query)
    return {**store.dict(), "id": last_record_id}

