from flask import Blueprint, render_template, request, redirect, session
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['user'] = user
            if user['role'] == 'admin':
                return redirect('/admin')
            elif user['role'] == 'recruiter':
                return redirect('/recruiter')
            else:
                return redirect('/candidate')

    return render_template('login.html')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name,email,password,role) VALUES (%s,%s,%s,%s)",
                       (name,email,password,role))
        db.commit()
        return redirect('/')

    return render_template('register.html')
