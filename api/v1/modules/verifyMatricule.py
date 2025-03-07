from flask import jsonify
from models import Instruction, Matricule, Module
from app import db

def verifyMatricule(module, matricule):
    query = (
        # Vérifie si le nom du module est présent, si le matricule existe et s'ils sont liés
        db.session.query(Matricule)
        .join(Module, Matricule.module_id == Module.id_)
        .filter(Module.nom == module, Matricule.numero == matricule)
        .first()
    )

    return jsonify(query is not None)  # Returne True si trouvé, False sinon. On doit évidemment jsonify le bool.


        
