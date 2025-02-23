from flask_restful import Resource, reqparse

# Datos en memoria (simulando base de datos)
tareas = []
tarea_id_count = 1

class gestion_tareas(Resource):
    def get(self):
        """Obtener todas las tareas"""
        return {"tareas": tareas}, 200

    def post(self):
        """Crear una nueva tarea"""
        global tarea_id_count
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, required=True, help="El título es obligatorio")
        parser.add_argument("description", type=str, required=True, help="La descripción es obligatoria")
        args = parser.parse_args()

        new_task = {"id": tarea_id_count, "titulo": args["title"], "descripcion": args["description"]}
        tareas.append(new_task)
        tarea_id_count += 1

        return {"Mensaje": "Tarea creada", "TAREA": new_task}, 201

    def delete(self, task_id):
        """Eliminar una tarea"""
        global tareas
        tareas = [task for task in tareas if task["id"] != task_id]
        return {"Mensaje": "Tarea eliminada"}, 200
