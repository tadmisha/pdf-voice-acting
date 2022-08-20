from PyPDF2 import PdfReader
from gtts import gTTS
import pathlib

def read_pdf(pdf_path):
    print('start reading pdf...')
    if not pathlib.Path(pdf_path).exists():
        return "This path is empty"
    else:
        if not pdf_path.endswith('.pdf'):
            return "This file is not pdf"
    pdf = PdfReader(pdf_path)
    text = ''
    for page_idx in range(pdf.numPages):
        text += pdf.getPage(page_idx).extractText()
    return text


def text_to_speech(speech_filename, text, lang):
    pass

def main():
    path = input('path to pdf file: ')
    text = read_pdf(path)

if __name__ == '__main__':
    main()