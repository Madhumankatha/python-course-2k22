from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    id:str
    bookname:str
    author:str
    price:int

app = FastAPI()
books = []
selectedBooks = []

@app.get("/")
def index():
    return {"message":"Welcome to Book Store!!!"}

@app.get("/bookstore")
def bookstore():
    return books

@app.post("/bookstore")
def addBook(book:Book):
    books.append(book)
    return book

@app.get("/billing")
def billing():
    data = []
    data.append(selectedBooks)
    total = sum(map(lambda b : b.price, selectedBooks ))
    data.append(dict({"total":total}))
    return data

@app.post("/billing/{id}")
def addBookToCart(id:int):
    selectedBook = getBookById(id);
    selectedBooks.append(selectedBook)
    return selectedBook

def getBookById(id) -> Book:
    return books[int(id)-1]
