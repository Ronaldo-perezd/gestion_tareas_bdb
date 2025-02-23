from flask_restful import Resource, reqparse
from models.tarea_model import Tarea
from flask import jsonify
from database import db  
from utils.autenticacion import autenticacion_simulada

class GestionTareas(Resource):
    
    @autenticacion_simulada    
    def get(self):
        """Obtener todas las tareas"""
        try:
            # 1 / 0  # ❌ Esto generará un error de división por cero (Internal Server Error)

            tareas = Tarea.query.all()
            return {"tareas": [tarea.to_dict() for tarea in tareas]}, 200
        except Exception as e:
            return ({"error": f"Error al obtener tareas: {str(e)}"}), 500
               
    @autenticacion_simulada
    def post(self):
        """Crear una nueva tarea"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("titulo", type=str, required=True, help="El título es obligatorio")
            parser.add_argument("descripcion", type=str, required=True, help="La descripción es obligatoria")
            args = parser.parse_args()
            
            # Validar que los valores no sean solo espacios en blanco
            titulo = args["titulo"].strip()
            descripcion = args["descripcion"].strip()
            
            if not titulo or not descripcion:
                return ({"error": "El título y la descripción no pueden estar vacíos"}), 400

            nueva_tarea = Tarea(titulo=args["titulo"], descripcion=args["descripcion"])
            db.session.add(nueva_tarea)
            db.session.commit()

            return {"mensaje": "Tarea creada", "tarea": nueva_tarea.to_dict()}, 201
        except Exception as e:
            return ({"error": f"Error al crear tarea: {str(e)}"}), 500
        
    @autenticacion_simulada
    def put(self, task_id):
        """Actualizar una tarea existente"""
        try:
            if task_id is None:
                return jsonify({"error": "Debes proporcionar un ID válido"}), 400
            
            tarea = db.session.get(Tarea, task_id) 
            if not tarea:
                return {"mensaje": "Tarea no encontrada"}, 404
            
            parser = reqparse.RequestParser()
            parser.add_argument("titulo", type=str, required=True, help="El título es obligatorio")
            parser.add_argument("descripcion", type=str, required=True, help="La descripción es obligatoria")
            args = parser.parse_args()

            tarea.titulo = args["titulo"]
            tarea.descripcion = args["descripcion"]
            db.session.commit()

            return {"mensaje": "Tarea actualizada", "tarea": tarea.to_dict()}, 200
        except Exception as e:
            return jsonify({"error": f"Error al actualizar tarea: {str(e)}"}), 500     
    
    @autenticacion_simulada
    def delete(self, task_id=None):
        """Eliminar una tarea"""
        try:
            if task_id is None:
                return jsonify({"error": "Debes proporcionar un ID válido"}), 400  # Devolver un error claro
            
            # tarea = Tarea.query.get(task_id)
            tarea = db.session.get(Tarea, task_id) 
            
            if tarea:
                db.session.delete(tarea)
                db.session.commit()
                return {"mensaje": "Tarea eliminada"}, 200
            return {"mensaje": "Tarea no encontrada"}, 404
        except Exception as e:
            return jsonify({"error": f"Error al eliminar tarea: {str(e)}"}), 500