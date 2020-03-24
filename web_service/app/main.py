from fastapi import FastAPI
import markovify
import requests
from text_maker.text_generator import TextGenerator

app = FastAPI()


@app.get("/get_gen_text")
def get_gen_text():
    text = TextGenerator()
    return {'text': text.generate()}



