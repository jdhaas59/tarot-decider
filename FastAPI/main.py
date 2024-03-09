from typing import Annotated
import httpx

import os
from dotenv import load_dotenv

from fastapi import FastAPI, Form
from deck import draw

from database import create_supabase_client
from models import User, Test

# from gotrue.exceptions import APIError



app = FastAPI()
sb = create_supabase_client()


@app.get("/")
def root():
    return {"message": "Hello World"}

 
@app.get('/draw')
async def draw_card():
    reading = draw()

    data = sb.table("readings").insert({
        "user_id":1,
        "first_card_name": reading[0].Card,
        "second_card_name": reading[1].Card,
        "third_card_name": reading[2].Card,
        "first_card_desc": reading[0].Meaning,
        "second_card_desc": reading[1].Meaning,
        "third_card_desc": reading[2].Meaning,
        }).execute()

    return data


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

    # try:
    #     session = sb.auth.sign_in_with_password({ "email": user_data.email, "password": user_data.password })
    # except APIError:
    #     print('Login Failed')
    session = sb.auth.sign_in_with_password({ "email": user_data.email, "password": user_data.password })
    return session


@app.post("/sign-out")
async def sign_out(user_data: User):

    # try:
    #     session = sb.auth.auth.sign_out({ "email": user_data.email, "password": user_data.password })
    # except APIError:
    #     print('Logout Failed')
    res = sb.auth.sign_out({ "email": user_data.email, "password": user_data.password })
    return res

