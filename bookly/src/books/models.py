from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, date
import uuid

class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str
    author: str
    publisher: str
    published_date: date
    pagecount: int
    language: str
    created_at: datetime = Field(default_factory=datetime.now, sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    updated_at: datetime = Field(default_factory=datetime.now, sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    
    
    def __repr__(self):
        return f"<Book {self.title}>"