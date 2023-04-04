from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Path
from src.repository import contacts as repository_contact
from src.schemas import ContactResponse, ContactModel
from sqlalchemy.orm import Session
from src.database.connector import get_db

router = APIRouter(prefix='/contacts', tags=['contacts'])
finder = APIRouter(prefix='/contacts/find', tags=['find'])


@router.get("/", response_model=List[ContactResponse])
async def get_all(db: Session = Depends(get_db)):
    contacts = await repository_contact.get_all(db)
    return contacts


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create(body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contact.find_by_email(body.email, db)
    if contact:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='some email use in '+contact.last_name)
    contact = await repository_contact.create(body, db)
    return contact


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_one(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contact.get_one(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contact.update(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contact.delete(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return contact


@finder.get("name/{contact_name}", response_model=ContactResponse)
async def find_by_name(contact_name: str, db: Session = Depends(get_db)):
    contact = await repository_contact.find_by_name(contact_name, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return contact


@finder.get("lastname/{lastname}", response_model=ContactResponse)
async def find_by_name(lastname: str, db: Session = Depends(get_db)):
    contact = await repository_contact.find_by_lastname(lastname, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return contact


@finder.get("email/{email}", response_model=ContactResponse)
async def find_by_name(email: str, db: Session = Depends(get_db)):
    contact = await repository_contact.find_by_email(email, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
    return contact


@finder.get("birthday/", response_model=List[ContactResponse])
async def get_all(db: Session = Depends(get_db)):
    contacts = await repository_contact.find_birthday7day(db)
    return contacts
