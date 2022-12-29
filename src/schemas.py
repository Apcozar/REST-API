from pydantic import BaseModel

class OutUser(BaseModel):
    name: str
    surname: str
    description: str

class InUser(BaseModel):
    name: str
    surname: str
    description: str