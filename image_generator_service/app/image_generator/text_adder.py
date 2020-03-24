from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class ImgEditor:

    def __init__(self, pic_path: str):
        self.img = Image.open(pic_path)
        self.draw_img = ImageDraw.Draw(self.img)
        self.font = self.set_font('fonts/lobster.ttf', 32)
        self.text_formator = TextFormat(self.img.height, self.img.width, self.font)

    def add_text(self, text: str):
        normalized_text = self.get_formated_text(text)
        coords_for_text = self.get_coords_for_text(text)
        self.draw_img.text(coords_for_text, normalized_text, (0, 0, 0), font=self.font)

    def get_formated_text(self, text):
        return self.text_formator.get_normalized_text(text)

    def get_coords_for_text(self, text):
        return self.text_formator.get_coords_for_text(text)

    def set_font(self, font_path: str, font_size: int) -> ImageFont:
        self.font = ImageFont.truetype(font_path, font_size)
        return self.font

    def save_pic(self, file_path: str):
        self.img.save(file_path)


class TextFormat:

    def __init__(self, pic_height: int, pic_width: int, font: ImageFont):
        self.pic_height = pic_height
        self.pic_width = pic_width
        self.font = font

    def get_normalized_text(self, text):
        len_of_sentence = 0
        output_sentence = ''
        for word in text:
            len_of_sentence += self.get_word_width(word)
            if len_of_sentence >= self.calculate_width_for_text():
                output_sentence += f'{word}-\n '
                len_of_sentence = 0
            else:
                output_sentence += f'{word}'
        return output_sentence

    def get_word_width(self, word):
        return self.font.getsize(word)[0]

    def get_word_height(self, word):
        return self.font.getsize(word)[1]

    def calculate_width_for_text(self) -> int:
        return self.pic_width - (self.pic_width // 8)

    def get_width_of_splitted_text(self, text):
        return self.get_word_width(self.get_normalized_text(text).split('\n')[0])

    def len_of_text(self, text):
        return len(self.get_normalized_text(text).split('\n'))

    def get_coords_for_text(self, text):
        x_coord = self.pic_width // 2 - self.get_width_of_splitted_text(text) // 2
        y_coord = (self.pic_height - self.pic_height // 30) - self.get_word_height(text) * self.len_of_text(text)
        return x_coord, y_coord

    def normalize_text(self):
        pass
