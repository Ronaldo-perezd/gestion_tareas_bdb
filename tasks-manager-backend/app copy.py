from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from rutas.tareas import gestion_tareas

app = Flask(__name__)   # Inicializa Flask
api = Api(app)          # Inicializa la API RESTful
CORS(app)               # Habilita CORS para permitir peticiones desde el frontend

# Registrar rutas
api.add_resource(gestion_tareas, "/tareas", "/tareas/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)  # Ejecutar en modo desarrollo
