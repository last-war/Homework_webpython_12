from src.database.models import Contact
from src.schemas import ContactModel
from sqlalchemy.orm import Session
from datetime import date, datetime


async def create(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def get_all(db: Session):
    contacts = db.query(Contact).all()
    return contacts


async def get_one(contact_id, db: Session):
    contact = db.query(Contact).filter(id=contact_id).first()
    return contact


async def update(contact_id, body: ContactModel, db: Session):
    contact = await get_one(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.birthday = body.birthday
        db.commit()
    return contact


async def delete(contact_id, db: Session):
    contact = await get_one(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def find_by_name(contact_name, db: Session):
    contact = db.query(Contact).filter(first_name=contact_name).first()
    return contact


async def find_by_lastname(lastname, db: Session):
    contact = db.query(Contact).filter(last_name=lastname).first()
    return contact


async def find_by_email(email, db: Session):
    contact = db.query(Contact).filter(email=email).first()
    return contact


async def find_birthday7day(db: Session):
    contacts = []
    db_contacts = db.query(Contact).all()
    today = date.today()
    for db_contact in db_contacts:
        birthday = db_contact.birthday
        shift = (datetime(today.year, birthday.month, birthday.day).date() - today).days
        if shift < 0:
            shift = (datetime(today.year + 1, birthday.month, birthday.day).date() - today).days
        if shift <= 7:
            contacts.append(db_contact)
    return contacts
