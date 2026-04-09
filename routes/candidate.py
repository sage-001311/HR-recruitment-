from flask import Blueprint, render_template, request, redirect, session
from db import get_db
import os
from config import UPLOAD_FOLDER

candidate_bp = Blueprint('candidate', __name__)

@candidate_bp.route('/candidate')
def candidate_dashboard():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    return render_template('candidate/dashboard.html', jobs=jobs)

@candidate_bp.route('/apply/<int:job_id>', methods=['POST'])
def apply(job_id):
    file = request.files['resume']
    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO applications (user_id,job_id,resume) VALUES (%s,%s,%s)",
                   (session['user']['id'], job_id, filename))
    db.commit()
    return redirect('/candidate')

@candidate_bp.route('/status')
def status():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM applications WHERE user_id=%s", (session['user']['id'],))
    apps = cursor.fetchall()
    return render_template('candidate/status.html', apps=apps)
