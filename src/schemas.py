from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    first_name: str = Field(max_length=150, min_length=1)
    last_name: str = Field(max_length=150, min_length=1)
    email: EmailStr
    phone: str = Field(max_length=14, min_length=6,
                       regex='\d{3}\-\d{3}\-\d{2}\-\d{2}|'
                             '\d{3}\-\d{3}\-\d{4}|'
                             '\(\d{3}\)\d{3}\-\d{2}\-\d{2}|'
                             '\(\d{3}\)\d{3}\-\d{4}|'
                             '\(\d{3}\)\d{7}|\d{10}|'
                             '\+\d{12}$')
    birthday: datetime


class ContactResponse(ContactModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: datetime

    class Config:
        orm_mode = True


class NoteModel(BaseModel):
    text: str = Field(max_length=1000, min_length=1)
    contact_id: int = Field(1, gt=0)


class NoteResponse(NoteModel):
    id: int
    text: str
    contact = ContactResponse

    class Config:
        orm_mode = True
