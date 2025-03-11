from flask import jsonify
from models import Niveau
from sqlalchemy import Select
from app import db

def  getNiveaux():
    stmt = (
        Select(Niveau)
    )

    liste = db.session.execute(stmt).scalars().all()
    
    if liste:
        return jsonify([{"id": niveau.id_, "nom": niveau.nom, "description": niveau.description, 
                 "duration": niveau.duration, "difficulty": niveau.difficulty, "color": niveau.color}
                 for niveau in liste]), 200
    else:
        return jsonify({"error": "Aucun niveau trouvé"}), 404
