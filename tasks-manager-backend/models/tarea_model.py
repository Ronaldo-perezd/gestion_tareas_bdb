from database import db  # Importamos `db` sin `app.py`

class Tarea(db.Model):
    __tablename__ = "tareas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "descripcion": self.descripcion}
