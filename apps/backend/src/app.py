from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}





# import pyttsx3
# engine = pyttsx3.init()  # object creation

# engine.save_to_file('hola, mi nombre es kevin y me gusta comer pan', 'test.mp3')
# engine.runAndWait()


# from deep_translator import GoogleTranslator
# to_translate = 'I want to translate this text'
# translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
# print(translated)
# outpout -> Ich möchte diesen Text übersetzen