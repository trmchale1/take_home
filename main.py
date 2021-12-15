from fastapi import FastAPI

app = FastAPI(title="Take Home")
metadata = sqlalchemy.MetaData()

store = sqlalchemy.Table(
    "store",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

engine = sqlalchemy.create_engine("postgresql://demouser:password123@127.0.0.1:5432/demo")

metadata.create_all(engine)

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

class StoreIn(BaseModel):
    name: str

class Store(BaseModel):
    id: int
    name: str

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.post("/store/", response_model=Store)
async def create_store(store: StoreIn):
    query = store.insert().values(name=store.name)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}
