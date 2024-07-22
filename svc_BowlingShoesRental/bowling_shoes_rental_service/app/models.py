from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    contact_info = Column(String)
    is_disabled = Column(Boolean)
    medical_conditions = Column(String)

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    rental_date = Column(DateTime)
    shoe_size = Column(String)
    rental_fee = Column(Float)
    discount = Column(Float)
    total_fee = Column(Float)

    customer = relationship("Customer")
