from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_marshmallow import Marshmallow
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm, TriviaForm

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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from models import User, Trivia
from user_schema import user_schema
from trivia_schema import trivia_schema

# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Handle registration logic
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/trivia/create', methods=['GET', 'POST'])
@login_required
def create_trivia():
    form = TriviaForm()
    if form.validate_on_submit():
        # Handle trivia creation logic
        trivia = Trivia(
            category=form.category.data,
            question=form.question.data,
            answer=form.answer.data,
            difficulty=form.difficulty.data,
            user=current_user
        )
        db.session.add(trivia)
        db.session.commit()
        flash('Trivia created successfully.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_trivia.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

