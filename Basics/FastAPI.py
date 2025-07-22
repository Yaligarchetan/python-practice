"""
Learning FastAPI Basics

Setup: Creating a Virtual Environment in Python

Commands:
    python -m venv venv                  # Create env
    venv\Scripts\activate (Windows)     # Activate env (Windows)
    source venv/bin/activate (Unix)     # Activate env (Mac/Linux)
    pip install fastapi uvicorn         # Install packages
    pip freeze > requirements.txt       # Save dependencies
    deactivate                         # Exit env

Running Your FastAPI App:
    uvicorn main:app --reload
    Visit http://127.0.0.1:8000/docs for interactive API docs.
"""

from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 1. What is FastAPI?
# FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+.
# It supports async programming, automatic docs generation, data validation with Pydantic, and more.

# 2. Creating FastAPI Applications with Path Operations (Routes)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

# HTTP Methods examples:
# @app.get()    - To get data from the server
# @app.post()   - To create new data on the server
# @app.put()    - To update existing data on the server
# @app.delete() - To delete data from the server

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}

# 3. Path and Query Parameters

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 4. Request Body and Response Models using Pydantic

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/pydantic/")
async def create_item_pydantic(item: Item):
    return item

# 5. Dependency Injection

def common_parameters(q: str = None):
    return q

@app.get("/search/")
async def search(q: str = Depends(common_parameters)):
    return {"q": q}

# 6. Middleware (Example: CORS)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; specify domains in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# 7. What is CORS?
# Cross-Origin Resource Sharing (CORS) is a security feature in browsers that restricts
# web applications from making requests to a different domain than the one that served the web page.
# Enabling CORS in FastAPI allows your frontend apps on other domains to access your API.

# 8. Background Tasks

def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message + "\n")

@app.post("/items/background/")
async def create_item_with_background_task(item: Item, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Item created: {item.name}")
    return item

# 9. Exception Handling

# Example in-memory items store
items = {
    1: {"name": "Foo", "price": 50.5},
    2: {"name": "Bar", "price": 30.0},
}

@app.get("/items/{item_id}/exception")
async def read_item_with_exception(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# 10. Running the Application
# Use the command below to run the FastAPI application:
# uvicorn main:app --reload
# Visit http://127.0.0.1:8000/docs for the interactive API documentation.

# 11. Additional Features
# FastAPI supports OAuth2, JWT authentication, WebSockets, and more.
# For more advanced features, refer to the FastAPI documentation at https://fastapi.tiangolo.com/

# 12. Testing the API
# You can test the API using tools like Postman, curl, or directly from the interactive docs at /docs.

# 13. Conclusion
# FastAPI is a powerful framework for building APIs quickly and efficiently.
