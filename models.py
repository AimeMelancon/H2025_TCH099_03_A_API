from app import db

class Niveau(db.Model):
    """Table niveau, qui contient les informations sur un niveau."""
    __tablename__ = 'niveau'

    id_ = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(6), nullable=False)

    # Relation many-to-many avec Module via la table Module_Niveau
    modules = db.relationship('Module', secondary='module_niveau', back_populates='niveaux')

    def __repr__(self):
        return f"Niveau {self.nom} avec id {self.id_}"
    


class Module(db.Model):
    """Table module, qui est liée à une instruction et à 1 ou plusieurs matricules."""
    __tablename__ = 'module'

    id_ = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(30), nullable=False)

    # Clé étrangère vers Instruction
    instructions_id = db.Column(db.Integer, db.ForeignKey('instructions.id_'), nullable=False)

    # Relation avec Matricule
    matricules = db.relationship('Matricule', backref='module', lazy='select')

    # Relation avec Niveau via Niveau-module
    niveaux = db.relationship('Niveau', secondary='module_niveau', back_populates='modules')

    def __repr__(self):
        return f"Module avec nom{self.nom} et instructions {self.instructions_id}"



class Module_Niveau(db.Model):
    """Table d'association entre Module et Niveau (Many-to-Many)."""
    __tablename__ = 'module_niveau'

    module_id = db.Column(db.Integer, db.ForeignKey('module.id_'), primary_key=True)
    niveau_id = db.Column(db.Integer, db.ForeignKey('niveau.id_'), primary_key=True)

    def __repr__(self):
        return f"Association Module {self.module_id} <-> Niveau {self.niveau_id}"


class Instruction(db.Model):
    """Table instructions, qui est liée à plusieurs modules."""
    __tablename__ = 'instructions'

    id_ = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    # Relation avec Module
    modules = db.relationship('Module', backref='instruction', lazy='select')

    def __repr__(self):
        return f"Instruction avec nom {self.nom} et description {self.description}"

class Matricule(db.Model):
    """Table matricule, qui est liée à module"""
    __tablename__ = 'matricule'

    numero = db.Column(db.String(6), primary_key=True)

    # Clé étrangère vers Module
    module_id = db.Column(db.Integer, db.ForeignKey('module.id_'), nullable=False)

    def __repr__(self):
        return f"Matricule {self.numero} relié au module {self.module_id}"