import os
import pytesseract
from PIL import Image


CURRENT_PATH = os.getcwd()
IMAGE_PATH = os.path.join(CURRENT_PATH, 'images')
TEXT_PATH = os.path.join(CURRENT_PATH, 'text')
VALID_FORMATS = ('jpg', 'jpeg', 'png')


def read_text_from_img(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def write_text_to_file(filename, text):
    file_path = os.path.join(TEXT_PATH, '{0}.txt'.format(filename))
    with open(file_path, 'w') as file:
        file.write(text)


def load_img_dir():
    for file in os.listdir(IMAGE_PATH):
        if file.split('.')[-1] not in VALID_FORMATS:
            continue
        filename = os.path.join(IMAGE_PATH, file)
        text = read_text_from_img(filename=filename)
        write_text_to_file(file.split('.')[0], text)


load_img_dir()
