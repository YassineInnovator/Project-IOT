from flask import Flask
from src.config.config import Config
from src.controllers.auth_controller import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(auth_bp)


#tbdeeel !!!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)