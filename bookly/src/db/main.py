from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine, text, SQLModel
from src.config import Config


# Cria o engine assíncrono corretamente
engine = AsyncEngine(
    create_engine(
        Config.DATABASE_URL,
        echo=True
    )
)

async def init_db():
    async with engine.begin() as conn:
       from src.books.models import Book
       
       await conn.run_sync(SQLModel.metadata.create_all) 
