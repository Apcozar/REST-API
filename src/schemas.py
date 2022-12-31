from pydantic import BaseModel

class OutUser(BaseModel):
    name: str
    surname: str
    description: str
    
    class Config:
        orm_mode = True


class InUser(BaseModel):
    name: str
    surname: str
    description: str

    class Config:
        orm_mode = True
