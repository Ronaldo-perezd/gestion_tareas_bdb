from functools import wraps
from flask import request, jsonify, make_response

def autenticacion_simulada(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Obtener el header Authorization
            auth_header = request.headers.get("Authorization")
            
            # Verificar si el header es correcto
            if not auth_header or auth_header != "token123":
                response = jsonify({"mensaje": "No autorizado"})  # Devuelve JSON
                return make_response(response, 401)  # Asegurar que Flask lo maneje correctamente

            return func(*args, **kwargs)

        except Exception as e:
            response = jsonify({"error": f"Error en autenticación: {str(e)}"})
            return make_response(response, 500)  # Asegurar que siempre devuelva JSON válido

    return wrapper