from fastapi import FastAPI
from app.routes import auth, tasks, notes

app = FastAPI(title="MindOrbit API")

app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(notes.router)

@app.get("/")
def read_root():
    return {"message": "MindOrbit API is live"}
