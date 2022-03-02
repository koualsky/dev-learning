from enum import Enum
from fastapi import FastAPI


class SelectNameModel(str, Enum):
    maciej = 'maciej'
    anthony = 'anthony'
    joe = 'joe'


app = FastAPI()


@app.get('/items/{item_id}')
async def get_item(item_id: int):
    return {'item_id': item_id}


# Watch what this do in docs. I have select automaticly!
@app.get('/models/{selected_model}')
async def get_model(selected_model: SelectNameModel):
    if selected_model == SelectNameModel.maciej:
        return {
            'selected_model': selected_model,
            'message': 'The best python proggrammer ever!'
        }

    if selected_model == SelectNameModel.anthony:
        return {
            'selected_model': selected_model,
            'message': 'The middle python dev dude.'
        }
    
    return {
        'selected_model': selected_model,
        'message': 'Very low quality programmer'
    }
