from flask_frozen import Freezer
from app import app  # Replace 'your_flask_app' with the name of your Flask app's module

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()