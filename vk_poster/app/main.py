from apicore import VkPoster
import json
import requests


def get_text_from_server():
    response = requests.get('http://127.0.0.1:5000/get_gen_text').text
    text = json.loads(response)
    generated_text = text['text']
    return generated_text


def make_post_in_group(text):
    vk_poster = VkPoster()
    vk_poster.make_post(text)


def start():
    text = get_text_from_server()
    if text is 'null':
        start()
    make_post_in_group(text)


