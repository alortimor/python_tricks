#!/usr/bin/python3
from datetime import datetime
from typing import List
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22',
                 'friends': [1, 2, 3]}
user = User(**external_data)

print("After assigning user")

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
    print("After initialising User")
except ValidationError as e:
    print("ValidationError")
    print(e.json())
