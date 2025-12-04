import uvicorn
from fastapi import FastAPI
from chatbot import response, teaching
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


 
origins = ["http://localhost:3000"]


app = FastAPI(version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

class Count(BaseModel):
    count: int

@app.get("/")
def home():
    return {"Message": "Welcome to our teaching assistant"}

@app.post("/solve")
def post(requests: Query):
    return {"Response:" : response(requests.question)}

@app.post("/teach")
def post_teach(requests: Query):
    return {"Response:": teaching(requests.question)}



if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8080)




