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
    print('finish reading pdf')
    print('start voice acting text...')
    if text=="This path is empty" or text=="This file is not pdf":
        lang='en'
    tts = gTTS(text, lang=lang, slow=False)
    tts.save(speech_filename)
    print('finish voice acting text')

def main():
    path = input('path to pdf file: ')
    lang = input('language code (for example en/ru/fr/de): ')
    speech_path = input('path to audio file: ')
    text = read_pdf(path)
    text_to_speech(speech_path, text, lang)

if __name__ == '__main__':
    main()