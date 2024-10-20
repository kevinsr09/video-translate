from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tts")
def read_item():
    return {"item_id": 1, "q": "1"}


# from deep_translator import GoogleTranslator
# to_translate = 'I want to translate this text'
# translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
# print(translated)
# outpout -> Ich möchte diesen Text übersetzen
