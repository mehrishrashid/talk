from flask import request, render_template, abort, send_file, jsonify
from gtts import gTTS
from app import app
from werkzeug.utils import secure_filename
import io
import os
import string
import random

from .utils import check_extention, check_language, image_ocr, pdf_ocr, TEMP_DIR, get_extention, IMAGE_EXTS, read_txt_file, text_to_speech

@app.errorhandler(400)
def bad_request( e):
  s = str(e)
  return jsonify(error=s[s.index(':') + 2:]), 400

@app.errorhandler(500)
def server_error(e):
  s = str(e)
  return jsonify(error=s[s.index(':') + 2:]), 500

@app.route('/', methods=['POST', 'GET'])
def index():
  # error = None
  if request.method == 'POST':
    try:
      uploaded_file = request.files['file']
      language = request.form['language']
      filename = secure_filename(uploaded_file.filename)

      if(check_extention(filename) and check_language(language)):
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8)) 
        filename = random_str + filename
        print(filename)

        print("[Index] Saving file..." + filename)
        uploaded_file.save(TEMP_DIR + filename)
        ext = get_extention(filename)
        text = ''
        
        if ext == '.pdf':
          print("[Index] Calling PDF Ocr..." + filename)
          text = pdf_ocr(TEMP_DIR + filename, language)
        elif ext in IMAGE_EXTS:
          print("[Index] Calling Image Ocr..." + filename)
          text = image_ocr(TEMP_DIR + filename, language)
        elif ext == '.txt':
          print("[Index] Calling Read Text File..." + filename)
          text = read_txt_file(TEMP_DIR + filename)
        
        if(text == '' or text == False):
          print("[Index - 400] 1. Something wrong with the input file. Couldn't convert to speech..." + filename)
          abort(400, description="Something wrong with the input file. Couldn't convert to speech");
        
        print("[Index] Calling TextToSpeech..." + filename)
        speech = text_to_speech(text, language)

        if(speech == False):
          print("[Index - 500] 1. Something went wrong. Couldn't convert to speech...." + filename)
          abort(500, description="Something went wrong. Couldn't convert to speech");

        try:   
          print("[Index] Saving mp3 file locally..." + filename)
          speech.save(TEMP_DIR + filename + '.mp3')
          mp3_file = io.BytesIO()
          
          with open(TEMP_DIR + filename + ".mp3", 'rb') as f:
            mp3_file.write(f.read())

          mp3_file.seek(0)
          
          os.remove(TEMP_DIR + filename + '.mp3')
          print("[Index] Removing mp3 file locally and sending to client from memory..." + filename)
          return send_file(mp3_file, mimetype="audio/mpeg", attachment_filename="file.mp3")
        except Exception as e:
          print("[Index] [Internal Server Error] Removing mp3 file..." + filename)
          os.remove(TEMP_DIR + filename + '.mp3')
          print(e)
          print("[Index - 500] 2. Something went wrong. Couldn't convert to speech...." + filename)
          abort(500, description="Something went wrong. Couldn't convert to speech")
        
      else:
        print("[Index - 400] 1. Something wrong with the input file or unsupported language...." + filename)
        abort(400, description="Something wrong with the input file or unsupported language.")
    except KeyError:
      print("[Index - 400] 2. Something wrong with the input file or unsupported language....")
      abort(400, description="Something wrong with the input file or unsupported language.")
    

  return render_template("index.html")
