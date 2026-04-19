from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register')
def register_page():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    users.append(data)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/sos', methods=['POST'])
def sos():
    data = request.json
    location = data.get("location", "Not available")
    return jsonify({"msg": "SOS Sent", "location": location})

if __name__ == "__main__":
    app.run()
