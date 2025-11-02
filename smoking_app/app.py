from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from smoking_app.models import db, User, Competition, CompetitionEntry
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret-key')
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///smoking_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.route('/')
    def index():
        competitions = Competition.query.all()
        return render_template('index.html', competitions=competitions)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if User.query.filter_by(username=username).first():
                flash('Username already exists')
                return redirect(url_for('signup'))
            user = User(username=username, password_hash=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('dashboard'))
        return render_template('signup.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            flash('Invalid credentials')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        competitions = Competition.query.all()
        return render_template('dashboard.html', competitions=competitions)

    @app.route('/competition/<int:competition_id>')
    @login_required
    def competition(competition_id):
        comp = Competition.query.get_or_404(competition_id)
        entries = CompetitionEntry.query.filter_by(competition_id=competition_id).all()
        return render_template('competition.html', competition=comp, entries=entries)

    @app.route('/join/<int:competition_id>')
    @login_required
    def join_competition(competition_id):
        comp = Competition.query.get_or_404(competition_id)
        if not CompetitionEntry.query.filter_by(user_id=current_user.id, competition_id=competition_id).first():
            entry = CompetitionEntry(user_id=current_user.id, competition_id=competition_id)
            db.session.add(entry)
            db.session.commit()
        return redirect(url_for('competition', competition_id=competition_id))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
