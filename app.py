# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html", 
    text="Serving up cool text from the Flask server!!")

@app.route("/file")
def file():
    return render_template("file.html", 
    text="File page")


if __name__ == "__main__":
    app.run(debug=True)