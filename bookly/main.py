from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allan B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "pagecount": 1234,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "pagecount": 1023,
        "language": "English"
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "pagecount": 3677,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "pagecount": 540,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "pagecount": 9282,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T. Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-21",
        "pagecount": 3006,
        "language": "English"
    }
]

@app.get('/books')
async def get_all_book():
    pass

@app.post('/books')
async def create_a_book() -> dict:
    pass

@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    pass

@app.get('/book/{book_id}')
async def update_book(book_id: int) -> dict:
    pass

@app.get('/book/{book_id}')
async def delete_book(book_id: int) -> dict:
    pass