from flask import Flask, request, jsonify, render_template , flash ,url_for ,redirect ,session
from flask_session import Session
from cs50 import SQL
from functools import wraps
import secrets

app = Flask(__name__)

# Generate a random 16-byte secret key
app.secret_key = secrets.token_hex(16)

# Use CS50's SQL library to connect to the database
db = SQL("sqlite:///mms.db") 

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("class_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

@app.route('/')
@login_required
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
        if not request.form.get("class_id"):
            flash("Select a class" , "danger")
            return redirect("/login")
        else:
            session["class_id"] = request.form.get("class_id")
            flash("Success !" , "success")
            return redirect("/")


@app.route("/register" , methods=["GET", "POST"])
def register():
    if request.method == "POST":
        className = request.form.get("class")
        level = str(request.form.get("level"))
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

@app.route("/percentage", methods=["GET", "POST"])
@login_required
def percentage():
    if request.method == "GET":
        num_of_sub = request.args.get('numOfSub', default=1, type=int)
        return render_template("percentage.html", num_of_sub=num_of_sub)

    if request.method == "POST":
        data = request.get_json()  # Safely retrieve JSON data
  
        if not data or 'num' not in data:
            return jsonify({"error": "No number provided"}), 400
        
        if data["num"] > ( data["num_of_sub"] * 100) :
            return jsonify({"error": "Invalid mark"}), 400

        try:
            num = int(data["num"])
            num_of_sub = int(data["num_of_sub"])
            percentage = num / num_of_sub 
            percentage_formatted = f"{percentage:.2f}"
        except ValueError:
            return jsonify({"error": "Invalid number format"}), 400


        # Process the number (your logic could go here, like database insertion)
        return jsonify({"result": f"{percentage_formatted} %"})

@app.route("/addmarks", methods=["GET", "POST"])
@login_required
def addmarks():
    if request.method == "GET":
        if request.args.get("subject") :
            subject = request.args.get("subject")
            updated_students = db.execute("SELECT MAX(student_id) AS last_student FROM students WHERE subject = ? AND class_id = ? ", subject , session["class_id"])     
            if updated_students[0]["last_student"] :
                student_id = int(updated_students[0]["last_student"])  + 1
            else:
                student_id = 1
            return render_template("addmarks.html" , student_id=student_id , subject=subject)
        else:
            class_id = session["class_id"]
            subjects_db = db.execute("SELECT name FROM  subjects WHERE level = (SELECT level FROM classes WHERE class_id = ?) ", class_id)
            return render_template("addmarks.html" , subjects_db=subjects_db , class_id=class_id )
        
    else:
        data = request.get_json()  # Safely retrieve JSON data
        marks = int(data["num"])
        subject = data["subject"]
        class_id = session["class_id"]
        if not data or 'num' not in data:
            return jsonify({"error": "No number provided"}), 400
        
        updated_students = db.execute("SELECT MAX(student_id) AS last_student FROM students WHERE subject = ? AND class_id = ? ", subject , class_id )     
        if updated_students[0]["last_student"] :
            student_id = int(updated_students[0]["last_student"])  + 1
        else:
            student_id = 1
        
        one = db.execute(
            "INSERT INTO students (student_id , class_id , subject , mark ) VALUES ( ? , ? , ? , ?)",
            student_id , class_id , subject , marks)

        student_id = student_id + 1
        # Process the number (your logic could go here, like database insertion)
        return jsonify({"marks" : f"{one}" , "subject" : f"{subject}", "current_student" : f"{student_id}" ,"clear_flash": True})


if __name__ == "__main__":
    app.run(debug=True ,host='0.0.0.0')