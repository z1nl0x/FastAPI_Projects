from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine, text, SQLModel
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

# Cria o engine assíncrono corretamente
async_engine = AsyncEngine(
    create_engine(
        Config.DATABASE_URL,
        echo=True
    )
)

async def init_db() -> None:
    async with async_engine.begin() as conn:
       from src.books.models import Book
       
       await conn.run_sync(SQLModel.metadata.create_all) 


async def get_session() -> AsyncSession:
    
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    
    async with Session() as session:
        yield session