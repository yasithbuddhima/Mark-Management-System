from flask import Flask, request, jsonify, render_template , flash ,url_for ,redirect
from flask_session import Session
from cs50 import SQL

import secrets


app = Flask(__name__)

# Generate a random 16-byte secret key
app.secret_key = secrets.token_hex(16)

# Use CS50's SQL library to connect to the database
db = SQL("sqlite:///mms.db")  # Make sure this points to your actual database file

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash_example')
def flash_example():
    flash('This is a flash message!', 'info')  # Flash a message
    flash('This is a flash message!', 'info')  # Flash a message
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True) 