from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from bowling_shoes_rental_service.app import models, schemas, crud, database

Fast_app = FastAPI()
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@Fast_app.post("/customers/", response_model=schemas.Customer)
def CreateCustomers(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

@Fast_app.post("/rentals/", response_model=schemas.Rental)
def CreateRental(rental: schemas.RentalCreate, db: Session = Depends(get_db)):
    return crud.create_rental(db=db, rental=rental)


@Fast_app.get("/customers/", response_model=list[schemas.Customer])
def ReadCustomers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers

@Fast_app.get("/rentals/", response_model=list[schemas.Rental])
def ReadRentals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rentals = crud.get_rentals(db, skip=skip, limit=limit)
    return rentals