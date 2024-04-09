import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str = Field(...)
    country: str = Field(...)

class Id(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    
class Student(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    age: int = Field(...)
    address: Address = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 20,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }

class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 20,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }