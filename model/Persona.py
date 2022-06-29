from pydantic import BaseModel
from fastapi import Form

class BasePersona(BaseModel):
    id:         int 
    name1:       str 
    name2:      str 
    surname1:   str 
    surname2:   str 