import streamlit as st
import streamlit.components.v1 as stc
import cv2
import numpy as np
# File Processing Pkgs
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber


class read_files:
    def __init__(self):
        self.image_file = None

    def read_pdf(self,file):
        pdfReader = PdfFileReader(file)
        count = pdfReader.numPages
        all_page_text = ''

        for i in range(count):
            page = pdfReader.getPage(i)
            all_page_text += page.extractText()

        return all_page_text

    def read_pdf_with_pdfplumber(self,file):
        with pdfplumber.open(file) as pdf:
            page = pdf.pages[0]
            return page.extract_text()

    @st.cache
    def load_image(self,image_file):
        img = Image.open(image_file)
        return img

    def file_info(self):
         self.file_details = {"Filename":self.image_file.name,"FileType":self.image_file.type,
                "FileSize":self.image_file.size}

    def read(self,choice):

        if choice == "Image":  

            st.subheader("Image")

            self.image_file = st.file_uploader("Upload Image", type=['png','jpeg','jpg'])

            if self.image_file is not None:
                # To See Details
                # st.write(type(image_file))
                # st.write(dir(image_file))

                self.file_info()
                st.write(self.file_details)

                # self.load_image(image_file)
                file_bytes = np.asarray(bytearray(self.image_file.read()), dtype=np.uint8)
                img = cv2.imdecode(file_bytes, 1)

                # Now do something with the image! For example, let's display it:
                # st.image(img, channels="BGR")
                # st.image(img,width=250,height=250)
                # st.image(img)
                return img

        # elif choice == "Dataset":
        #     st.subheader("Dataset")
        #     data_file = st.file_uploader("Upload CSV",type=['csv'])
        #     if st.button("Process"):
        #         if data_file is not None:
        #             file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
        #             st.write(file_details)

        #             df = pd.read_csv(data_file)
        #             st.dataframe(df)

        # elif choice == "DocumentFiles":
        #     st.subheader("DocumentFiles")
        #     docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
        #     if st.button("Process"):
        #         if docx_file is not None:
        #             file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
        #             st.write(file_details)
        #             # Check File Type
        #             if docx_file.type == "text/plain":
        #                 # raw_text = docx_file.read() # read as bytes
        #                 # st.write(raw_text)
        #                 # st.text(raw_text) # fails
        #                 st.text(str(docx_file.read(),"utf-8")) # empty
        #                 raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for futher processing
        #                 # st.text(raw_text) # Works
        #                 st.write(raw_text) # works
        #             elif docx_file.type == "application/pdf":
        #                 # raw_text = read_pdf(docx_file)
        #                 # st.write(raw_text)
        #                 try:
        #                     with pdfplumber.open(docx_file) as pdf:
        #                         page = pdf.pages[0]
        #                         st.write(page.extract_text())
        #                 except:
        #                     st.write("None")
                            
                        
        #             elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        #             # Use the right file processor ( Docx,Docx2Text,etc)
        #                 raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class directory
        #                 st.write(raw_text)

        # else:
        #     st.subheader("About")
        #     st.info("Built with Streamlit")
        #     st.info("Jesus Saves @JCharisTech")
        #     st.text("Jesse E.Agbe(JCharis)")



# if __name__ == '__main__':
    # main()