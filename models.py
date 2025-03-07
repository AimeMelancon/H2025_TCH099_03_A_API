from app import db

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


class Module(db.Model):
    """Table module, qui est liée à une instruction."""
    __tablename__ = 'module'

    id_ = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(30), nullable=False)

    # Clé étrangère vers Instruction
    instructions_id = db.Column(db.Integer, db.ForeignKey('instructions.id_'), nullable=False)

    # Relation avec Matricule
    matricules = db.relationship('Matricule', backref='module', lazy='select')

    def __repr__(self):
        return f"Module avec nom{self.nom} et instructions {self.instructions_id}"


class Matricule(db.Model):
    """Table matricule, qui est liée à module"""
    __tablename__ = 'matricule'

    numero = db.Column(db.String(6), primary_key=True)

    # Clé étrangère vers Module
    module_id = db.Column(db.Integer, db.ForeignKey('module.id_'), nullable=False)

    def __repr__(self):
        return f"Matricule {self.numero} relié au module {self.module_id}"