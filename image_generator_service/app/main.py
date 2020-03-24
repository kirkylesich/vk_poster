from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from image_generator.text_adder import ImgEditor
import random

app = FastAPI()


@app.get('/get_image/{text}')
def get_random_image(text):
    pic_name = create_pic_with_text(text)
    return {'pic_link': f'/images/{pic_name}', 'pic_name': pic_name}


app.mount("/images", StaticFiles(directory="generated_images"), name="static_images")


def get_random_pic(pic_count):
    random_num = random.randrange(1, pic_count, 1)
    return f'{random_num}.jpg'


def create_pic_with_text(text):
    pic_name = get_random_pic(13)
    img_editor = ImgEditor(f'static_images/{pic_name}')
    img_editor.add_text(text)
    output_pic_name = f'{random.randrange(1, 100, 1)}'
    img_editor.save_pic(f'generated_images/{output_pic_name}.jpg')
    return f'{output_pic_name}.jpg'
