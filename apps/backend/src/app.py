from fastapi import FastAPI
from src.presentation.routes import router
app = FastAPI()

app.include_router(router)

# from deep_translator import GoogleTranslator
# to_translate = 'I want to translate this text'
# translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
# print(translated)
# outpout -> Ich möchte diesen Text übersetzen
