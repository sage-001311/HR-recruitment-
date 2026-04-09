from flask import Flask
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.recruiter import recruiter_bp
from routes.candidate import candidate_bp

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(recruiter_bp)
app.register_blueprint(candidate_bp)

if __name__ == "__main__":
    app.run(debug=True)
