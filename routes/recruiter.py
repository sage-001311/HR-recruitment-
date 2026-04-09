from flask import Blueprint, render_template, request, redirect, session
from db import get_db

recruiter_bp = Blueprint('recruiter', __name__)

@recruiter_bp.route('/recruiter')
def recruiter_dashboard():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    return render_template('recruiter/dashboard.html', jobs=jobs)

@recruiter_bp.route('/applications/<int:job_id>')
def view_applications(job_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM applications WHERE job_id=%s", (job_id,))
    apps = cursor.fetchall()
    return render_template('recruiter/applications.html', apps=apps)

@recruiter_bp.route('/update_status/<int:id>', methods=['POST'])
def update_status(id):
    status = request.form['status']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE applications SET status=%s WHERE id=%s", (status,id))
    db.commit()
    return redirect(request.referrer)

@recruiter_bp.route('/add_job', methods=['POST'])
def add_job():
    title = request.form['title']
    desc = request.form['description']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO jobs (title,description) VALUES (%s,%s)", (title,desc))
    db.commit()
    return redirect('/recruiter')
