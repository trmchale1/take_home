from fastapi import FastAPI

app = FastAPI(title="Take Home")


@app.get("/")
def read_root():
    return {"hello": "world"}
