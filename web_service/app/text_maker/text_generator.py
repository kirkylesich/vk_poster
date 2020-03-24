import markovify
import requests


class TextGenerator:

    def __init__(self):
        self.text_file = self.get_txt_file()
        self.text_maker = markovify.Text(self.text_file)

    def generate(self):
        text = self.text_maker.make_sentence()
        return text

    def get_txt_file(self):
        return requests.get('https://raw.githubusercontent.com/kirkylesich/datasets/master/aneks.txt').text

