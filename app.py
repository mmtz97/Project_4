# import necessary libraries
# from tkinter import image_names
from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from pathlib import Path
from PIL import Image, ExifTags

# create instance of Flask app
app = Flask(__name__)
app.config['UPOADED_IMAGE'] = join(dirname(realpath(__file__)), 'static/uploads/..')
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def foo():
    bar = "Worlld Hello"
    return bar

def adding(name):
    print('Run me' + name)
    img = Image.open(name)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    return exif

# create route that renders index.html template
@app.route('/')
def index():
    print("Main")
    return render_template("index.html", value1=foo)


# Route for displaying and saving uploaded image
@app.route("/", methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["UPOADED_IMAGE"], image.filename))
            test = os.path.join(app.config["UPOADED_IMAGE"], image.filename)
            text = 'I think I found me'
            print("I am in the upload")
            return render_template("index.html", uploaded_image=image.filename, value1 = adding(test))
    print("I am before second return")        
    return render_template("index.html", value1 = text)



# Route for displaying uploaded picture
# no longer needed - keeping for the time being will delete in cleanup for turn in
# TODO: Delete me later
@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    text = 'hi'
    return send_from_directory(app.config["UPOADED_IMAGE"], filename)

# TODO: Need a route to return a string
# Will be streamlined into the upload route once it is working
# Should return accucry of model based on picture.



@app.route('/test')
def test():
    return render_template('test.html')



@app.route('/test', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        adding(uploaded_file.filename)
    else:
        print("Nothing Selected")
    return redirect(url_for('test'))



if __name__ == "__main__":
    app.run(debug=True)






