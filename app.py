from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import numpy as np 
import pandas as pd 
import cv2
from random import randint
from audio import encode
from audio import decode
from text import encode_data
from text import decode_data
from image import merge
from image import unmerge


app= Flask(__name__)

# s1=cv2.imread("s1.png")
# s2=cv2.imread("s.png")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/image')
def image():
    
    merge('3.png','5.png')
    return "who let the dogs out "
    
@app.route('/decode')
def imagedecode():
    unmerge('merged.png')
    return "u cant kill me"

@app.route('/audio')
def audio():
    encode()
    decode()
    return render_template('cool.html')
 
@app.route('/', methods=['POST','GET'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        last_name = request.form.get("fname") 
        print(last_name)
        file.save(file.filename)
        img = cv2.imread(file.filename)
        encode_data(img,last_name)
        image1=cv2.imread("s.png")
        decode_data(image1)
        return render_template('cool.html')



if __name__ == "__main__":
    app.run()
