from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from models import db, User

bcrypt = Bcrypt()

class AuthService:
    @staticmethod
    def register(username, password):
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully"}

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)
            return {"token": token}
        return {"error": "Invalid credentials"}, 401
