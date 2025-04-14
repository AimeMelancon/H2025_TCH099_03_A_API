from app import create_app, db
flask_app = create_app()
import os
from dotenv import load_dotenv

debug_mode = os.getenv("DEBUG")


# Crée les tables (seulement si elles n'existent pas déjà)
with flask_app.app_context():
    db.create_all()

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Savoir à partir du .env si on est en debug ou pas
debug_mode = os.getenv("DEBUG", "False").lower() == "true"

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=debug_mode)