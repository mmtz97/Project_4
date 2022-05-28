# import necessary libraries
from flask import Flask, render_template, request
import os
from os.path import join, dirname, realpath

# create instance of Flask app
app = Flask(__name__)
app.config['UPOADED_IMAGE'] = join(dirname(realpath(__file__)), 'static/uploads/..')

# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html", 
    text="Serving up cool text from the Flask server!!")

@app.route("/file")
def file():
    return render_template("file.html", 
    text="File page")

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["UPOADED_IMAGE"], image.filename))
            return render_template("file.html", uploaded_image=image.filename)
    return render_template("file.html")


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPOADED_IMAGE"], filename)


if __name__ == "__main__":
    app.run(debug=True)