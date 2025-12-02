import uvicorn
from fastapi import FastAPI
from chatbot import response, teaching
from dotenv import load_dotenv
from pydantic import BaseModel


app = FastAPI(version="1.0.0")

class query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"Message": "Welcome to our teaching assistant"}

@app.post("/solve")
def post(requests: query):
    return {"Response:" : response(requests.question)}

@app.post("/teach")
def post_teach(requests: query):
    return {"Response:": teaching(requests.question)}

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8080)




