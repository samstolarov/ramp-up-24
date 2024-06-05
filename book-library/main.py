from fastapi import FastAPI

app = FastAPI()

books = []
next_id = 1

#create books
@app.post("/books/")
async def create_book(title:str, author:str, year:int):
    global next_id
    new_book = {
        "id" : next_id,
        "title" : title,
        "author" : author,
        "year" : year
    }
    books.append(new_book)
    next_id += 1
    return new_book

#get all books
@app.get("/books/")
def get_books():
    return books

#get specific book
@app.get("/books/{id}")
def get_specific_book(id : int):
    for book in books:
        if book['id'] == id:
            return book
#update book
@app.put("/books/{id}")
def update_book(id : int, title:str, author:str, year:int):
    for book in books:
        if book["id"] == id:
            book["title"] = title
            book["author"] = author
            book["year"] = year
            return book
#delete books
@app.delete("/books/{id}")
def delete_book(id:int):
    global books
    for book in books:
        if book["id"] == id:
            books = [b for b in books if b['id'] != id]
            return books

