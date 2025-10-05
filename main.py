from fastapi import FastAPI, templating

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}