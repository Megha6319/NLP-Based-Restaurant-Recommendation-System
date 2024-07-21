from flask import Flask, json, jsonify, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if username in users:
            flash('Username already exists!', 'error')
            return redirect(url_for('signup'))
        
        users[username] = {
            'password': password,
            'email': email
        }
        flash('Signup successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username not in users or users[username]['password'] != password:
            flash('Invalid username or password!', 'error')
            return redirect(url_for('login'))
        
        session['username'] = username
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('index.html')

@app.route('/recommendations')
def recommendations():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('recommendations.html')

@app.route('/data')
def data():
    try:
        with open('top_recommended_restaurants.json', 'r') as file:
            data = json.load(file)
        
        # Extract only restaurant names
        restaurants = [entry.get('Restaurant') for entry in data if 'Restaurant' in entry]
        
        return jsonify(restaurants)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
