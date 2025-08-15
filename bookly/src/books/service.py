from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select, desc
from .models import Book
from datetime import datetime, date

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        books = result.all()
        
        # Converte todas as datas para string
        for book in books:
            book.published_date = book.published_date.isoformat()
        
        return books
    
    async def get_book(self, book_uid:str, session:AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        
        result = await session.exec(statement)
        
        book = result.first()
        
        book.published_date = book.published_date.isoformat()
        
        return book if book is not None else None
    
    async def create_book(self, book_data: BookCreateModel, session:AsyncSession):
        book_data_dict = book_data.model_dump()
        
        new_book = Book(**book_data_dict)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        
        # Converte o date de volta para string (para o schema de resposta)
        new_book.published_date = new_book.published_date.isoformat()  # Formato "YYYY-MM-DD"
        
        return new_book
    
    async def update_book(self, book_uid:str, update_data:BookUpdateModel, session:AsyncSession):
        book_to_update = self.get_book(book_uid, session)
        
        if book_to_update is not None:
        
            update_data_dict = update_data.model_dump()
            
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)
            
            await session.commit()
            
            return book_to_update
        else:
            return None
    
    async def delete_book(self, book_uid:str, session:AsyncSession):
        book_to_delete = self.get_book(book_uid, session)
        
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            
            await session.commit()
            
            return {}
        else:
            return None
    