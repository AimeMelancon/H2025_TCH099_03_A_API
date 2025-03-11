from flask import jsonify
from sqlalchemy import Select
from models import Matricule, Module
from app import db

def verifyMatricule(module, matricule):
    stmt = (
        # Vérifie si le nom du module est présent, si le matricule existe et s'ils sont liés
        Select(Matricule)
        .join(Module, Matricule.module_id == Module.id_)
        .filter(Module.nom == module, Matricule.numero == matricule)
    )

    result = db.session.execute(stmt).scalars().first()

    return jsonify(result is not None)  # Returne True si trouvé, False sinon. On doit évidemment jsonify le bool.


        
