from app import create_app, db
from models import Matricule, Module, Instruction, Niveau, Module_Niveau

flask_app = create_app()


# Crée les tables (seulement si elles n'existent pas déjà)
with flask_app.app_context():
    db.create_all()

    # --------- Jeu de test temporaire dans la DB ---------------
    db.session.query(Module_Niveau).delete()
    db.session.query(Matricule).delete()
    db.session.query(Module).delete()
    db.session.query(Instruction).delete()
    db.session.query(Niveau).delete()

    # 🔹 Ajout des Instructions
    instruction1 = Instruction(nom="Intro", description="Learn Flask basics")
    instruction2 = Instruction(nom="Database", description="Introduction to SQLAlchemy and database relations")
    instruction3 = Instruction(nom="Flask", description="Working with Blueprints, Middleware, and API Development")

    db.session.add_all([instruction1, instruction2, instruction3])
    db.session.commit()  # Commit pour générer les IDs

    # 🔹 Ajout des Modules liés aux Instructions
    module1 = Module(nom="Flask", schema="schema_1", instructions_id=instruction1.id_)
    module2 = Module(nom="SQL", schema="schema_2", instructions_id=instruction2.id_)
    module3 = Module(nom="API", schema="schema_3", instructions_id=instruction3.id_)

    db.session.add_all([module1, module2, module3])
    db.session.commit()

    # 🔹 Ajout des Matricules liés aux Modules
    matricule1 = Matricule(numero="ABC123", module_id=module1.id_)
    matricule2 = Matricule(numero="XYZ789", module_id=module2.id_)
    matricule3 = Matricule(numero="LMN456", module_id=module3.id_)

    db.session.add_all([matricule1, matricule2, matricule3])
    db.session.commit()

    # 🔹 Ajout des Niveaux
    niveau1 = Niveau(nom="Beginner", description="Basic concepts", duration=30, difficulty="Easy", color="00FF00")
    niveau2 = Niveau(nom="Intermediate", description="Intermediate topics", duration=60, difficulty="Medium", color="FFFF00")
    niveau3 = Niveau(nom="Advanced", description="Advanced Flask and SQLAlchemy", duration=90, difficulty="Hard", color="FF0000")

    db.session.add_all([niveau1, niveau2, niveau3])
    db.session.commit()

    # 🔹 Création des relations many-to-many (Module ↔ Niveau)
    module_niveau1 = Module_Niveau(module_id=module1.id_, niveau_id=niveau1.id_)
    module_niveau2 = Module_Niveau(module_id=module2.id_, niveau_id=niveau2.id_)
    module_niveau3 = Module_Niveau(module_id=module3.id_, niveau_id=niveau3.id_)
    module_niveau4 = Module_Niveau(module_id=module3.id_, niveau_id=niveau2.id_)  # Un module peut appartenir à plusieurs niveaux

    db.session.add_all([module_niveau1, module_niveau2, module_niveau3, module_niveau4])
    db.session.commit()




if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=True)