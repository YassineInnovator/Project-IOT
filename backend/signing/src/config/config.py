class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@db:5432/signing_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False