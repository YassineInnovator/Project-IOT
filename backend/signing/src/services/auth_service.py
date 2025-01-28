import redis
from src.models.user import User, db
from flask_jwt_extended import create_access_token # type: ignore

# Initialize Redis client
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

def create_user(username, password):
    user = User(username=username, password=password) # type: ignore
    db.session.add(user)
    db.session.commit()
    # Optionally, store user session in Redis
    redis_client.set(f'session:{username}', password)  # Example of storing user session
    return user

def authenticate_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        token = create_access_token(identity=user.username)
        return token
    return None