from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
import os
from database import db  # Importa db desde el nuevo módulo
from rutas.tareas import GestionTareas # Importamos las rutas después de inicializar `db`

# Inicializa Flask
app = Flask(__name__)
api = Api(app)
CORS(app)

# Configuración de SQLite
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join("/tmp", "tareas.db")  #Guarda la BD en /tmp/

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "bd_app/tareas.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Vincular db con la app de Flask
db.init_app(app)

# Registrar la API
api.add_resource(GestionTareas, "/tareas", "/tareas/<int:task_id>")

# funcion global para errores internos del servidor (500)
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Error interno del servidor", "detalle": str(error)}), 500

# funcion global para rutas no encontradas (404)
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado. Verifica la URL y el método HTTP"}), 404

# funcion para solicitudes incorrectas (400)
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Solicitud incorrecta"}), 400

# Asegurar la creación de la BD antes de iniciar el servidor
with app.app_context():
    db.create_all()  # Crea la BD si no existe

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()  # Crea la BD si no existe
    # app.run(port=8077, debug=True)
    port = int(os.environ.get("PORT", 5000))  # Render usa una variable de entorno para el puerto
    app.run(host="0.0.0.0", port=port, debug=True)
    