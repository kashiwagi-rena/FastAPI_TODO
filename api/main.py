from fastapi import FastAPI

app = FastAPI()

@app.get("/Hello_Word")
def read_root():
    return {"Hello": "World"}