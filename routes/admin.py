from flask import Blueprint, render_template
from db import get_db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin_dashboard():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM jobs")
    jobs = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM applications")
    apps = cursor.fetchone()[0]

    return render_template('admin/dashboard.html', users=users, jobs=jobs, apps=apps)

