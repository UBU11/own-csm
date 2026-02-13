from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/api/v1/hello")
def read_hello():
    return {"message": "Hello form FastAPI"}
