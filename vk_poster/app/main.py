from apicore import VkPoster
import json
import requests
import urllib
import os

def get_text_from_server():
    response = requests.get('http://127.0.0.1:5000/get_gen_text').text
    text = json.loads(response)
    generated_text = text['text']
    if generated_text is None:
        get_text_from_server()
    return generated_text


def get_pic_from_server(text):
    response = requests.get(f'http://127.0.0.1:5001/get_image/{text}').text
    text = json.loads(response)
    img_link = text['pic_link']
    img_name = text['pic_name']
    img = requests.get(f'http://127.0.0.1:5001{img_link}').content
    create_dir_for_pics()
    with open(f'generated_images/{img_name}', 'wb') as f:
        f.write(img)

    return img_name

def create_dir_for_pics():
    try:
        os.mkdir('generated_images')
    except FileExistsError:
        pass

def get_pic_with_text():
    generated_text = get_text_from_server()
    pic_name = get_pic_from_server(generated_text)
    return pic_name


def make_post_in_group():
    pic_path = f'generated_images/{get_pic_with_text()}'
    text = get_text_from_server()
    vk_poster = VkPoster()
    vk_poster.make_post(text, pic_path)


def start():
    make_post_in_group()
