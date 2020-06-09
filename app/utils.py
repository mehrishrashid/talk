import os
import cv2
import pytesseract
import numpy as np
from pdf2image import convert_from_path
from gtts import gTTS

FILE_EXTS = ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.pdf', '.txt']
IMAGE_EXTS = ['.jpeg', '.jpg', '.png', '.gif', '.bmp']
TEMP_DIR = 'app/temp/'
ACCEPTABLE_LANGUAGES = ['eng', 'urd', 'hin','fra']

def get_extention(filename):
  return os.path.splitext(filename)[1]

def check_extention(filename, FILE_EXTS = FILE_EXTS):
  return get_extention(filename) in FILE_EXTS

def check_language(language):
  return language in ACCEPTABLE_LANGUAGES

def image_ocr(file, language):
  if(check_extention(file, IMAGE_EXTS)):
    try:
      print("[Image Ocr] OpenCV image read.. " + file)
      image = cv2.imread(file)
      print("[Image Ocr] OpenCV converting to inverted GrayScale.. " + file)
      gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
      gray = cv2.bitwise_not(gray)

      print("[Image Ocr] OpenCV Eroded and dilated to remove noise.. " + file)
      kernel = np.ones((2, 1), np.uint8)
      image = cv2.erode(image, kernel, iterations=1)
      image = cv2.dilate(image, kernel, iterations=1)

      print("[Image Ocr] Image to text (pytessaract).. " + file)
      text = pytesseract.image_to_string(image, lang=language)

      print("[Image Ocr] Removing file.. " + file)
      os.remove(file)
      text = text.replace('-\n', '')
      return text
    except Exception as e:
      print("[Image Ocr] [Internal Server Error] Removing file.. " + file)
      os.remove(file)
      print(e)
      return False
  else:
    print("[Image Ocr] [File/language unsupported] Removing file.. " + file)
    os.remove(file)
    return False

def pdf_ocr(file, language):
  if(check_extention(file, FILE_EXTS=['.pdf'])):
    try:
      base = os.path.basename(file)
      name = os.path.splitext(base)[0]

      print("[PDF Ocr] Getting pdf pages.. "+ name)
      pages = convert_from_path(file, 500)
      image_counter = 1

      for page in pages: 
        filename = name + "page_" + str(image_counter) + ".jpg"

        print("[PDF Ocr] Saving pdf pages as Images.. " + filename)
        page.save(TEMP_DIR + filename, 'JPEG')
        image_counter += 1
      
      filelimit = image_counter-1
      text = ''

      for i in range(1, filelimit + 1): 
        filename = TEMP_DIR + name + "page_" + str(i) + ".jpg"
        
        print("[PDF Ocr] Getting text from Images (invoking image_ocr method).. " + filename)
        text += image_ocr(filename, language)

      print("[PDF Ocr] Removing File.. " + file)
      os.remove(file)
      return text
    except Exception as e:
      print("[PDF Ocr] [Internal Server Error] Removing File.. " + file)
      os.remove(file)
      print(e)
      return False
  else: 
    print("[PDF Ocr] [File/language unsupported] Removing File.. " + file)
    os.remove(file)
    return False
  
def read_txt_file(file):
  text = ''
  print("[Text File] Reading file.. " + file)
  with open(file) as f:
    text = f.read() 

  print("[Text File] Removing file.. " + file)
  os.remove(file)
  return text

def text_to_speech(text, language):
  if(text and language in ACCEPTABLE_LANGUAGES):
    if language == 'eng':
      language = 'en'
    elif language == 'hin':
      language = 'hi'
    elif language == 'urd':
      language = 'ur'
    elif language == 'fra':
      language = 'fr'
  
    try:
      print("[TextToSpeech] Getting speech from gTTS.. ")
      speech = gTTS(text = text, lang = language)
      return speech
    except Exception as e:
      print("[TextToSpeech] [Internal server error] Return.. ")
      print(e)
      return False
  else:
    print("[TextToSpeech] [No Text/Language unsupported] [Internal server error] Return.. ")
    False

