from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret_key')  # Set a secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')  # Set the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Load environment variables from .env file
load_dotenv('.env')

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize other packages
ma = Marshmallow(app)
csrf = CSRFProtect(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Trivia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('trivia', lazy=True))

# Import the route handlers
from routes.users import users_bp
from routes.trivia import trivia_bp

# Register the route blueprints
app.register_blueprint(users_bp)
app.register_blueprint(trivia_bp)

