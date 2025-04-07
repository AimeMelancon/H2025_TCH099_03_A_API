from app import create_app, db
flask_app = create_app()


# Crée les tables (seulement si elles n'existent pas déjà)
with flask_app.app_context():
    db.create_all()


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=False)