from typing import Annotated
import httpx

import os
from dotenv import load_dotenv

from fastapi import FastAPI, Form
from deck import draw

from database import create_supabase_client
from models import User, Test



app = FastAPI()
sb = create_supabase_client()


@app.get("/")
def root():
    return {"message": "Hello World"}

 
@app.get('/draw')
def draw_card():
    return draw()


@app.post("/test-add")
async def add_test(test_data: Test):

    res = sb.table("test").insert({"name":test_data.name}).execute()

    return res

# USERS
@app.post("/sign-up")
async def create_user(user_data: User):

    res = sb.auth.sign_up({ "email": user_data.email, "password": user_data.password })

    return res


@app.post("/sign-in")
async def sign_in(user_data: User):

    session = sb.auth.sign_in_with_password({ "email": user_data.email, "password": user_data.password })

    return session

