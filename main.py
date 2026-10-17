from fastapi import FastAPI
from fastapi import  Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app =FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title":"favourite foods", "content": "I like pizza", "id": 2}]


# request comes with Get methods url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my API!!!!!"}

@app.get("/posts")
def get_posts():
    return{"data": "This is your posts"}

@app.post("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)

    my_posts.append(post_dict)
    return{"data": post_dict}


@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return{"post_detail": f"Here is post {id}"}
#title str, content str 