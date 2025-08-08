from pydantic import BaseModel
import uuid
from datetime import datetime, date

class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    pagecount: int
    language: str
    created_at: datetime
    updated_at: datetime
    
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    pagecount: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    pagecount: int
    language: str