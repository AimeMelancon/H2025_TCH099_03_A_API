from flask import jsonify
from models import Instruction, Matricule, Module
from app import db

def getInstruction(matricule):
    query = (
        db.session.query(Instruction)
        .join(Module, Module.instructions_id == Instruction.id_)
        .join(Matricule, Matricule.module_id == Module.id_)
        .filter(Matricule.numero == matricule)
        .first()
    )

    if query:
        return jsonify({"id": query.id_, "nom": query.nom, "description": query.description}), 200
    else:
        return jsonify({"error": "Instruction non trouvee."}), 404