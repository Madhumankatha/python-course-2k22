from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
books = []
selectedBooks = []

class Book(BaseModel):
    id:int
    name:str
    author:str
    price:int


@app.get("/")
def index():
    return {"message":"Welcome to bookstore!!"}

@app.get("/books")
def getAllBooks():
    return books

@app.post("/books")
def addNewBook(book:Book):
    books.append(book)
    return book

@app.get("/billing")
def getSelectedItems():
    data = []
    data.append(selectedBooks)
    total = sum(map(lambda b:b.price, selectedBooks)) 
    data.append({"total":total})
    return data

@app.post("/billing/{id}")
def addToCart(id:int):
    book = getBookById(id)
    selectedBooks.append(book)
    return book

def getBookById(id):
    return books[int(id)-1]