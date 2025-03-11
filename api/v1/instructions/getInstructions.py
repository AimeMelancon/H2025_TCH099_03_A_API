from flask import jsonify
from sqlalchemy import Select
from models import Instruction, Matricule, Module

from app import db

def getInstruction(matricule):
    stmt = (
        Select(Instruction)
        .join(Module, Module.instructions_id == Instruction.id_)
        .join(Matricule, Matricule.module_id == Module.id_)
        .filter(Matricule.numero == matricule)
    )

    result = db.session.execute(stmt).scalars().first()

    if result:
        return jsonify({"id": result.id_, "nom": result.nom, "description": result.description}), 200
    else:
        return jsonify({"error": "Instruction non trouvee."}), 404