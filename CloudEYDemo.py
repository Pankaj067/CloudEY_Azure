from flask import Flask, render_template
import sys, string, os


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World, This is Azure!!'



if (__name__ == "__main__"):
    app.run(debug=True)