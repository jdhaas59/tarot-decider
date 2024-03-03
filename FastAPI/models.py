from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class Test(BaseModel):
    name: str