import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return "This page is not completed yet. Visit Later."
  return render_template("login.html")

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8001)