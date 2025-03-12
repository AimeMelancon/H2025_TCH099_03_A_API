from flask import jsonify
from sqlalchemy import Select
from models import Instruction, Matricule, Module

from app import db

def getInstruction(matricule):
    """Récupère les instructions apartenant à un certain matricule.

    
    Route associée: '/api/v1/instructions/<matricule>', méthodes: GET

    Paramètres: 
      matricule (str): Le matricule lui-même, qui est un string d'une longueur de 6 charactères.

    Retour:
      Si le matricule existe: 
        {"description": [...], "id": [...], "nom": [...]}
        Réponse HTTP: 200 OK

      Sinon:
        {"error": "Aucun niveau trouvé"}
        Réponse HTTP: 404 Not Found
    """
    
    # Requête SQL
    stmt = (
        Select(Instruction)
        .join(Module, Module.instructions_id == Instruction.id_)
        .join(Matricule, Matricule.module_id == Module.id_)
        .filter(Matricule.numero == matricule)
    )

    # Exécution de la requête
    result = db.session.execute(stmt).scalars().first()

    # Retour
    if result:
        return jsonify({"id": result.id_, "nom": result.nom, "description": result.description}), 200
    else:
        return jsonify({"error": "Instruction non trouvée."}), 404