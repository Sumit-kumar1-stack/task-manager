from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    email:str
    password:str

class Login(BaseModel):
    username:str
    password:str

class TaskCreate(BaseModel):
    title:str
    description:str

class TaskResponse(TaskCreate):
    id:int

    class Config:
        from_attributes = True