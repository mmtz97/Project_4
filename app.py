# import necessary libraries
# from tkinter import image_names
from flask import Flask, render_template, request
import os
from os.path import join, dirname, realpath
from pathlib import Path

# create instance of Flask app
app = Flask(__name__)
app.config['UPOADED_IMAGE'] = join(dirname(realpath(__file__)), 'static/uploads/..')

# create route that renders index.html template
@app.route("/upload", methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["UPOADED_IMAGE"], image.filename))
            return render_template("upload.html", uploaded_image=image.filename)
    return render_template("upload.html")

# Show a list of images.
@app.route("/files")
def file():
    # image_names = join(dirname(realpath(__file__)), 'static/uploads')
    # return render_template("files.html", image_name = image_names)
    basepath = f"static/uploads"
    dir = os.walk(basepath)
    file_list = []

    for path, files in dir:
        for file in files:
            temp = path.joinPath(path + '/', file)
            file_list.append(temp)
            print(file_list + "hello")
    return render_template('files.html', hists=file_list)

# Route for displaying and saving uploaded image
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["UPOADED_IMAGE"], image.filename))
            return render_template("index.html", uploaded_image=image.filename)
    return render_template("index.html")


# Route for displaying uploaded picture
@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPOADED_IMAGE"], filename)


if __name__ == "__main__":
    app.run(debug=True)