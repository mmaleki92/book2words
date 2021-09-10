from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import multiprocessing
import os
from file_reader import read_files
from ocr import ocr
import re
from googletrans import Translator

"""

# book2words 
convert your book/article to a bunch of words to learn the meaning of each word and read your material faster!

"""

class main_app:
    def __init__(self):
        self.file = None
        self.choice = ''
        self.read_class = read_files()
    def page_interface(self):
        st.title("File Upload Tutorial")
        menu = ["Image","Dataset","DocumentFiles","About"]
        self.choice = st.sidebar.selectbox("Menu",menu)

        # self.reader = read_files
    def run(self):

        self.page_interface()

        img = self.read_class.read(self.choice)

        if st.button('Generate words'):

            if(img is not None):
                    words = ocr(img)

                    # print(words)
                    words = [word for word in words if(all(re.findall("[a-zA-Z]", word)) and len(word)>1 )]
                    st.write(words)

                    st.write(pd.DataFrame(words))
            else:
                st.write("Please choose an appropriate format!")

if __name__ == '__main__':
    # main_app().run()
    translator = Translator()
    result = translator.translate('Mitä sinä teet')
    print(result.text)

    