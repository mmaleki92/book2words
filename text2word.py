try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pdf2image


# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('bader.pdf',output_folder = './output_article',dpi=200, fmt='JPEG', transparent =False
,thread_count = 3,last_page = 344)
print('done reading!')
# for i in range(10):
#       # Save pages as images in the pdf
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')


