from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Initialise le framework Flask. Retourne l'application flask."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
    app.config['secret_key'] = "C'est un secret"
    
    
    app.json.sort_keys = False # Retourne les json en ordre de la base de données, pas alphabétique
    app.json.ensure_ascii = False # Désacive ASCII, utilise plutôt UTF-8. Formattage des accents...

    db.init_app(app)

    from routes import initialize_routes
    initialize_routes(app)

    return app

