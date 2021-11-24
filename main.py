from functools import reduce
from typing import List, Optional
import requests
from fastapi import FastAPI
import celery

import tasks

app = FastAPI()





@app.get("/")
def index():
    return {"Message" : "Hello World!"}


@app.get("/calculate/{a}/{b}")
async def sum_function(a:int, b:int) -> int:
    '''
    This endpoint calculates the value of the sum of the two path parameters
    :param a: first number
    :param b: second number
    :return: integer
    '''
    return a+b

@app.get("/calculate/")
async def sum_function_query(a:int, b:int) -> int:
    '''
    This endpoint calculates the value of the sum of the two path parameters
    :param a: first number
    :param b: second number
    :return: integer
    '''
    return a+b

@app.post("/sumall")
async def sum_function_rb(body: List[int]) -> int :
    return reduce(lambda x,y: x+y, body)


@app.get("/sleep")
async def sleep(duration:Optional[int] = 5):
    tasks.sleep_task.delay(duration)
    return {"Message":"OK"}