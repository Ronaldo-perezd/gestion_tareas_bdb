import unittest
import sys
import os
from models.tarea_model import Tarea  # Importar el modelo Tarea

# Agregar el directorio raíz al sys.path para que pytest encuentre `app.py`
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from app import app, db

class BaseTestCase(unittest.TestCase):
    """Clase base para configurar pruebas"""

    @classmethod
    def setUpClass(cls):
        """Ejecuta antes de todas las pruebas"""
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Base de datos en memoria
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()
            
    def setUp(self):
        """Se ejecuta antes de cada test: Vacía la BD"""
        with app.app_context():
            db.session.query(Tarea).delete()
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Ejecuta después de todas las pruebas"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()