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

if __name__ == '__main__':
    directory  = 'output_article'
    # directory = 'output/'

    pages = 5
    set_words = set()
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