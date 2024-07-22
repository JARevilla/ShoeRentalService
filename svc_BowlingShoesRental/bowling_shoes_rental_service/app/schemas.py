from pydantic import BaseModel
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    age: int
    contact_info: str
    is_disabled: bool
    medical_conditions: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class RentalBase(BaseModel):
    customer_id: int
    rental_date: datetime
    shoe_size: str
    rental_fee: float
    discount: float
    total_fee: float

class RentalCreate(RentalBase):
    pass

class Rental(RentalBase):
    id: int

    class Config:
        orm_mode = True
