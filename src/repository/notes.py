from src.database.models import Note
from src.schemas import NoteModel
from sqlalchemy.orm import Session


async def create(body: NoteModel, db: Session):
    note = Note(**body.dict())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


async def get_all(db: Session):
    notes = db.query(Note).all()
    return notes


async def get_one(note_id, db: Session):
    note = db.query(Note).filter(id=note_id).first()
    return note


async def update(note_id, body: NoteModel, db: Session):
    note = await get_one(note_id, db)
    if note:
        note.text = body.text
        db.commit()
    return note


async def delete(note_id, db: Session):
    note = await get_one(note_id, db)
    if note:
        db.delete(note)
        db.commit()
    return note

