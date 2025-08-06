from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from src.config import Config

# Cria o engine assíncrono corretamente
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)

async def init_db():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 'hello';"))
        print(result.all())
