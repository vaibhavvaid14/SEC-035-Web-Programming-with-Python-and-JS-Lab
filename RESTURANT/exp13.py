from flask import Flask, render_template_string, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(_name_)
app.secret_key = 'secret123'

# Setup Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize Database
def init_db():
    with sqlite3.connect("users.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )''')

init_db()

# WTForms
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

# User class for Flask-Login
class User(UserMixin):
    def _init(self, id, username, role):
        self.id = id_
        self.username = username
        self.role = role
    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    with sqlite3.connect("users.db") as conn:
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        if user:
            return User(user[0], user[1], user[3])
    return None

# Routes
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        try:
            with sqlite3.connect("users.db") as conn:
                conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                             (form.username.data, hashed, "user"))
            flash("User created! Now login.", "success")
            return redirect(url_for('login'))
        except:
            flash("Username already exists!", "danger")
    return render_template_string(SIGNUP_TEMPLATE, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with sqlite3.connect("users.db") as conn:
            user = conn.execute("SELECT * FROM users WHERE username = ?", (form.username.data,)).fetchone()
            if user and check_password_hash(user[2], form.password.data):
                login_user(User(user[0], user[1], user[3]))
                return redirect(url_for('dashboard'))
        flash("Invalid username or password", "danger")
    return render_template_string(LOGIN_TEMPLATE, form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == "admin":
        return f"<h2>Welcome Admin: {current_user.username}</h2> <a href='/logout'>Logout</a>"
    return f"<h2>Welcome User: {current_user.username}</h2> <a href='/logout'>Logout</a>"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# HTML Templates (inline)
LOGIN_TEMPLATE = '''
<h2>Login</h2>
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.username.label }} {{ form.username() }}<br>
  {{ form.password.label }} {{ form.password() }}<br>
  {{ form.submit() }}
</form>
<a href="/signup">Sign up</a>
'''

SIGNUP_TEMPLATE = '''
<h2>Sign Up</h2>
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.username.label }} {{ form.username() }}<br>
  {{ form.password.label }} {{ form.password() }}<br>
  {{ form.submit() }}
</form>
<a href="/login">Login</a>
'''

if _name_ == "_main_":
    app.run(debug=True)
