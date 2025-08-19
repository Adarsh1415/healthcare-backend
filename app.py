from flask import Flask
from config import Config
from models.user import db, bcrypt, User
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()
        # Create default admin if not exists
        if not User.query.filter_by(role='admin').first():
            hashed_pw = bcrypt.generate_password_hash('password').decode('utf-8')
            admin_user = User(username='admin', password=hashed_pw, role='admin')
            db.session.add(admin_user)
            db.session.commit()
    return app

#adding logger
#main app
#init.py add

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
