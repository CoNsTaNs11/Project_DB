from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):

    name: str
    description: str
    danger_level: str
    event_type: str
    city: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
