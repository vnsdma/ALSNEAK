from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask import send_from_directory

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
# Definisi Model

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

# Routes
if __name__ == '__main__':
    app.run(debug=True)
