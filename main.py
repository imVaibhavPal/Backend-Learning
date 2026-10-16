from fastapi import FastAPI
from fastapi import  Body
from pydantic import BaseModel


app =FastAPI()


class Post(BaseModel):
    title: str
    content: str
    

# request comes with Get methods url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my API!!!!!"}

@app.get("/posts")
def get_posts():
    return{"data": "This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.title)
    return{"data":"new post"}

#title str, content str