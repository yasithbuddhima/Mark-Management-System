from flask import Flask, request, jsonify, render_template , flash ,url_for ,redirect ,session
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

@app.route("/login" , methods=["GET", "POST"])
def login():
    if request.method == "GET":
        class_db = db.execute("SELECT * FROM classes")
        if not class_db :
            flash("No classes added yet. Add new class","danger")
            return redirect("/register")
        else:
            return render_template("login.html" , class_db=class_db)
    else:
        session["class_id"] = request.form.get("class_id")
        flash("Success !" , "success")
        return redirect("/")


@app.route("/register" , methods=["GET", "POST"])
def register():
    if request.method == "POST":
        className = request.form.get("class")
        level = request.form.get("level")
        term = request.form.get("term")
        year = request.form.get("year")

        if not term or not level :
            flash("Please fill out all fields","danger")
            return render_template("register.html")
        else:
            check_user = db.execute(
                "SELECT * FROM classes WHERE class = ? AND term = ? AND year = ? AND level = ?",
                className , term , year , level)
           
            if check_user:
                flash("Class is already exist.","success")
                session["class_id"] = check_user
                return redirect("/")
            new_class = db.execute(
                "INSERT INTO classes (class , term , year , level) VALUES (?,?,?,?)",
                className, term , year , level
            )
            session["class_id"] = new_class
            flash( term + " of " + className + " class added successfully", "info")   
            return redirect("/")
    else:
        return render_template("register.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/login")

@app.route('/flash_example')
def flash_example():
    flash('This is a flash message!', 'info')  # Flash a message
    flash('This is a flash message!', 'info')  # Flash a message
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0')