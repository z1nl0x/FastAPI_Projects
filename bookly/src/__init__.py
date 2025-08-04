from fastapi import FastAPI
from src.books.routes import book_router 

versionapp = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API fora book review web service",
    version=versionapp
)

app.include_router(book_router, prefix=f"/api/{versionapp}/books", tags=['books'])