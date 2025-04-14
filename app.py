from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os 

db = SQLAlchemy()

def create_app():
    """Initialise le framework Flask. Retourne l'application flask."""
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

    # Load la clé secrète du fichier .env
    secret_key = os.getenv("SECRET_KEY")

    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
    app.config['secret_key'] = secret_key
    
    
    app.json.sort_keys = False # Retourne les json en ordre de la base de données, pas alphabétique
    app.json.ensure_ascii = False # Désacive ASCII, utilise plutôt UTF-8. Formattage des accents...

    db.init_app(app)

    from routes import initialize_routes
    initialize_routes(app)

    return app

