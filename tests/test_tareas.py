import unittest
import json
import sys
import os
from app import app, db  # Importar app y db para manipular la base de datos
from models.tarea_model import Tarea  # Importar el modelo Tarea


# Agregar la raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))
from tests.test_app import BaseTestCase

class TestTareas(BaseTestCase):
    """Pruebas para la API de Tareas"""

    def test_crear_tarea(self):
        """Prueba la creación de una tarea"""
        with app.app_context():
            db.session.query(Tarea).delete()  # Elimina todas las tareas antes de la prueba
            db.session.commit()
            
        response = self.client.post(
            "/tareas",
            headers={"Content-Type": "application/json", "Authorization": "token123"},
            data=json.dumps({"titulo": "Tarea 1", "descripcion": "Descripción de la tarea 1"})
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Tarea creada", response.get_data(as_text=True))

    def test_obtener_tareas(self):
        """Prueba obtener la lista de tareas (debe estar vacía inicialmente)"""        
        response = self.client.get(
            "/tareas",
            headers={"Authorization": "token123"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["tareas"], [])

    def test_eliminar_tarea(self):
        """Prueba eliminar una tarea inexistente"""
        response = self.client.delete(
            "/tareas/9999",
            headers={"Authorization": "token123"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("Tarea no encontrada", response.get_data(as_text=True))

    def test_autenticacion_fallida(self):
        """Prueba la autenticación con token incorrecto"""
        response = self.client.get("/tareas", headers={"Authorization": "incorrecto"})
        self.assertEqual(response.status_code, 401)
        self.assertIn("No autorizado", response.get_data(as_text=True))
    
    def test_actualizar_tarea(self):
        """Prueba actualizar una tarea existente"""
        with app.app_context():  # Asegura que la BD opere dentro de un contexto válido

            # Crear una tarea primero
            tarea_nueva = Tarea(titulo="Tarea Original", descripcion="Descripción original")
            db.session.add(tarea_nueva)
            db.session.commit()

            # Realizar la actualización
            response = self.client.put(
                f"/tareas/{tarea_nueva.id}",
                headers={"Content-Type": "application/json", "Authorization": "token123"},
                data=json.dumps({"titulo": "Tarea Modificada", "descripcion": "Descripción modificada"})
            )

            self.assertEqual(response.status_code, 200)
            self.assertIn("Tarea actualizada", response.get_data(as_text=True))

            # Verificar que la tarea fue actualizada en la BD
            tarea_actualizada = db.session.get(Tarea, tarea_nueva.id)
            self.assertEqual(tarea_actualizada.titulo, "Tarea Modificada")
            self.assertEqual(tarea_actualizada.descripcion, "Descripción modificada")
        
        
if __name__ == "__main__":
    unittest.main()