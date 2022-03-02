from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

async def read_something(pk, sec):  # 1. to moze byc funkcja scrappujaca cos, lub pobierajaca cos z db lub file.
    await asyncio.sleep(sec)
    result = f'I was {pk} and I an done!'
    print(result)
    return result

@app.get('/')
async def index():
    # result = await read_something(1, 4)
    # result = await read_something(2, 3)
    # result = await read_something(3, 5)
    # result = await read_something(4, 1)
    futures = [
        read_something(1, 4), 
        read_something(2, 3), 
        read_something(3, 5), 
        read_something(4, 1)
    ]
    a, b, c, d = await asyncio.gather(*futures)  # 2. a tu gatherujemy wyniki i przychodza tak jak sie pobiora :)
    result = 'end'
    return {'message': result}


# Normalnie synchronicznie powinno to zajac 13 sekund
# Asynchronicznie - 5 sekund
# RUN: uvicorn simplest:app --reload