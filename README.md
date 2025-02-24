# Tasks Manager API

## Descripción

Esta API permite gestionar tareas mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar).&#x20;

Está construida con Flask y Flask-RESTful, y utiliza una base de datos SQLAlchemy.

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Ronaldo-perezd/gestion_tareas_bdb
cd tasks-manager-backend
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv nombre_entorno

nombre_entorno\Scripts .\activate
```

### 3. Instalar dependencias

```bash
pip install -r requerimientos.txt
```

### 4. Configurar la base de datos

Verifica y modificar `app.py` con la URI de la base de datos:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "bd_app/tareas.db")
```

### 5. Ejecutar migraciones (si se usa Flask-Migrate)

```bash
flask db upgrade
```

### 6. Iniciar la API

En una terminal ejecutar el siguiente comando:

```bash
flask run --host=0.0.0.0 --port=5000
```

O en su defecto ejecutar el archivo de configuración de la API:

```bash
python app.py
```

## Endpoints de la API

### 1. Obtener todas las tareas

**GET** `/tareas`

```json
{
  "tareas": [
    {
      "id": 1,
      "titulo": "Comprar carne",
      "descripcion": "1 kg de carne molida en la carniceria"
    }
  ]
}
```

### 2. Crear una nueva tarea

**POST** `/tareas`

```json
{
  "titulo": "comprar carne",
  "descripcion": "1 kg de carne molida en la carniceria"
}
```

**Respuesta:**

```json
{
  "mensaje": "Tarea creada",
  "tarea": {
    "id": 1,
    "titulo": "comprar carne",
    "descripcion": "1 kg de carne molida en la carniceria"
  }
}
```

### 3. Actualizar una tarea

**PUT** `/tareas/{id}`

```json
{
  "titulo": "Comprar carne molida de cerdo",
  "descripcion": "1 lb de carne molida de cerdo"
}
```

**Respuesta:**

```json
{
  "mensaje": "Tarea actualizada",
  "tarea": {
    "id": 1,
    "titulo": "Comprar carne molida de cerdo",
    "descripcion": "1 lb de carne molida de cerdo"
  }
}
```

### 4. Eliminar una tarea

**DELETE** `/tareas/{id}`

```json
{
  "mensaje": "Tarea eliminada"
}
```

## Pruebas

Para ejecutar las pruebas unitarias con `unittest` o `pytest`:

```bash
pytest tests/
```

Se debe visualizar algo como:

```bash
============================================================ test session starts =============================================================

platform win32 -- Python 3.12.1, pytest-8.3.4, pluggy-1.5.0

rootdir: D:\tasks-manager-backend

collected 5 items                                                                                                                            

tests\test\_tareas.py .....                                                                                                              [100%]

============================================================= 5 passed in 5.51s =============================================================
```

Si se quieren ver de forma individual ejecuta en la terminal el comando:

```bash
pytest -v tests/
```

Y se observará de la siguiente forma:

```bash
================================================================================ test session starts =================================================================================

platform win32 -- Python 3.12.1, pytest-8.3.4, pluggy-1.5.0 -- D:\Scripts\python.exe

cachedir: .pytest\_cache

rootdir: D:\tasks-manager-backend

collected 5 items                                                                                                                                                                    


tests/test_tareas.py::TestTareas::test_actualizar_tarea PASSED                                                                                                                  [ 20%]

tests/test_tareas.py::TestTareas::test_autenticacion_fallida PASSED                                                                                                             [ 40%]

tests/test_tareas.py::TestTareas::test_crear_tarea PASSED                                                                                                                       [ 60%]

tests/test_tareas.py::TestTareas::test_eliminar_tarea PASSED                                                                                                                    [ 80%]

tests/test_tareas.py::TestTareas::test_obtener_tareas PASSED                                                                                                                    [100%]


================================================================================= 5 passed in 2.91s ==================================================================================
```

## Autenticación

Cada solicitud debe incluir un token en los headers:

```
Authorization: token123
```

## Errores y Manejo de Excepciones

- **400**: Datos inválidos o faltantes.
- **404**: Tarea no encontrada.
- **500**: Error interno del servidor (manejado con `@app.errorhandler(500)`).

## Herramientas recomendadas

- Thunder Client o Postman para probar la API.
- SQLite o PostgreSQL como base de datos.
- Flask-Migrate para gestión de migraciones.

---

Desarrollado por **Ronaldo Pérez D.**

