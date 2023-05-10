import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the relative file path for the database
db_file_path = os.path.join(current_dir, 'market.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file_path}'
# TODO: find a way to fix the db_file_path when uploading

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file_path}'
app.config['SECRET_KEY'] = 'ba15d2f8ad72cdc515988647'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()