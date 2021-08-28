import os
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
import pytesseract
import cv2


def words_list(page_image):

    custom_config = r'--oem 3 --psm 6'
    page = pytesseract.image_to_string(page_image, config=custom_config)

    blob = TextBlob(page)

    word_list = blob.words.lemmatize()
    # blob.noun_phrases 
    return word_list

def ocr(img):
    directory  = 'output_article'
    # directory = 'output/'
    pages = 5

    set_words = set()

    if (img == None):
        all_files = os.listdir(directory)
        for filename in all_files[:pages]:
                if filename.endswith(".jpg"):
                    print(filename)
                    image = cv2.imread('output_article/' +filename)

                    new_words = words_list(image)
                    set_words = set_words.union(set(new_words))
                    # print(new_words)
                # break
                # print(set_words)
                print(len(set_words))
    else:
        image = img # cv2.imread(img)
        new_words = words_list(image)
        set_words = set_words.union(set(new_words))
    return set_words
