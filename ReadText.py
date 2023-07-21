import pytesseract
from PIL import Image
import cv2
import re
from pytesseract import Output
import os


class ReadText:
    def __init__(self, img):
        self.img = img

    def english(self):
        text = pytesseract.image_to_string(self.img, lang='eng')
        return text


    def find(self, text):
        d = pytesseract.image_to_data(self.img, output_type=Output.DICT)
        # keys = list(d.keys())
        date_pattern = text
        date_pattern_lower = text.lower()
        date_pattern_upper = text.upper()
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if float(d['conf'][i]) > 60:
                if re.match(date_pattern_lower, d['text'][i]) or re.match(date_pattern_upper, d['text'][i]) or re.match(
                        date_pattern, d['text'][i]):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    img = cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return Image.fromarray(self.img)

    def number(self):
        text = pytesseract.image_to_string(self.img, lang='eng')
        words = text.split()
        number_pattern = r'\d+'
        numbers_found = []
        for word in words:
            match = re.search(number_pattern, word)
            if match:
                numbers_found.append(match.group())
        return numbers_found
    


    def phonenumber(self):
        text = pytesseract.image_to_string(self.img, lang='eng')
        words = text.split()
        pattern = r'\+?(\d{2,3}[-) ]\d{3,4}[- ]\d{4,5})'
        phone_numbers = []
        for word in words:
            numbers_in_word = re.findall(pattern, word)
            if numbers_in_word:
                phone_numbers.extend(numbers_in_word)

        return phone_numbers
