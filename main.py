# python -m venv fastapi

from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"HEY": "All"}


@app.get('/a')
def a():
    return {"zd": "a"}
