from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="safety_app"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register')
def reg_page():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():
    d = request.form
    cursor.execute(
        "INSERT INTO users(name,email,phone,password,emergency) VALUES(%s,%s,%s,%s,%s)",
        (d['name'], d['email'], d['phone'], d['password'], d['emergency'])
    )
    db.commit()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    d = request.form
    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (d['email'], d['password'])
    )
    if cursor.fetchone():
        return redirect('/dashboard')
    return "Invalid login"

@app.route('/dashboard')
def dash():
    return render_template("dashboard.html")

@app.route('/sos', methods=['POST'])
def sos():
    data = request.json
    loc = data.get("location","NA")
    return jsonify({"msg":"SOS Sent","loc":loc})

@app.route('/poweroff', methods=['POST'])
def power():
    print("Power off detected")
    return "ok"

app.run(debug=True)
