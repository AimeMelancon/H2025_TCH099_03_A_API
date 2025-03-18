from flask import jsonify

from models import TraductionMatricule, InstructionsDescriptions, PatPlayInstructions1, PatPlayInstructions2
from sqlalchemy import Select
from app import db

def getInstructions(module, matricule):
    # Requête SQL
    stmt = (
        Select(TraductionMatricule)
        .filter(TraductionMatricule.idMatricule == matricule, TraductionMatricule.nomModule == module)
    )
    # Exécution de la requête
    result = db.session.execute(stmt).scalars().first()

    if result is None:
        return jsonify({"result": False}), 404

    # Cas spécial: PatPlay
    if module == 'PatPlay':

        # Requêtes SQL
        stmt_desc = (Select(InstructionsDescriptions.description)
                    .filter(InstructionsDescriptions.nomModule == 'PatPlay'))

        stmt_inst1 = Select(PatPlayInstructions1)
        stmt_inst2 = Select(PatPlayInstructions2)


        # Exécution des requêtes
        patplay_description = db.session.execute(stmt_desc).scalars().first()
        patplay_instructions1 = db.session.execute(stmt_inst1).scalars().all()
        patplay_instructions2 = db.session.execute(stmt_inst2).scalars().all()

        
        patplay_instructions1 = [
            {
                "id": inst.id_,
                "couleur": inst.couleur,
                "carre": inst.carre,
                "cercle": inst.cercle,
                "triangle": inst.triangle,
                "x": inst.x
            }
            for inst in patplay_instructions1
        ]

        patplay_instructions2 = [
            {
                "id": inst.id_,
                "nbFinal": inst.nbFinal,
                "ordre": inst.ordre
            }
            for inst in patplay_instructions2
        ]

        return jsonify({
            'description': patplay_description,
            "instructions1": patplay_instructions1,
            "instructions2": patplay_instructions2
        }), 200
    
    # Fetch description & instructions des autres module que PatPlay
    else:
        # String table d'instructions à accéder
        tablename = f'{module}Instructions1'


        # Requêtes SQL
        stmt_desc = (Select(InstructionsDescriptions.description)
                    .filter(InstructionsDescriptions.nomModule == module))
        
        description = db.session.execute(stmt_desc).scalars().first()
        

        # Récupérer la table à accéder selon le module en argument
        table = db.Model.metadata.tables.get(tablename)

        # Récupère les instructions
        stmt_instructions = Select(table)
        results = db.session.execute(stmt_instructions).all()

        # Transformer chaque résultat de la requête en un dictionnaire
        instructions = [dict(row._mapping) for row in results]

        return jsonify({"description": description, "instructions": instructions}), 200
        
        



            

        
