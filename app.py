import uvicorn
from fastapi import FastAPI
from chatbot import response, teaching
from dotenv import load_dotenv


app = FastAPI(version="1.0.0")

@app.get("/")
def home():
    return {"Message": "Welcome to our teaching assistant"}

@app.post("/solve")
def post(requests: str):
    return {"Response:" : response(requests)}

@app.post("/teach")
def post_teach(requests: str):
    return {"Response:": teaching(requests)}

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8080)




