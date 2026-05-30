from fastapi import FastAPI

from database import Base, engine
from routers import users, tasks

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {
        "message": "Task Manager API Running"
    }
