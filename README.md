# 🎓 Microservicios Colegio

Este proyecto consiste en una arquitectura basada en microservicios utilizando **FastAPI**, **MySQL** y **Docker**. Se han desarrollado dos microservicios:

- 📘 `estudiante-service`: Gestión de estudiantes
- 📗 `evaluacion-service`: Gestión de evaluaciones

Todo el sistema se orquesta con `docker-compose`.

---

## 🚀 Tecnologías Utilizadas

- Python 3.10
- FastAPI
- Uvicorn
- SQLAlchemy
- MySQL 8
- Docker y Docker Compose

---

## 🐳 Cómo levantar el proyecto

1. Asegúrate de tener **Docker** y **Docker Compose** instalados.
2. Clona este repositorio.
3. Ejecuta en la raíz del proyecto:
```bash
docker-compose down -v  # por si se quiere reiniciar completamente la BD
docker-compose up --build
```

🛠️ Endpoints
📘 Estudiante Service – http://localhost:8001
🔹 Obtener todos los estudiantes
Método: GET

URL: /estudiantes

🔹 Obtener un estudiante por RUT
Método: GET

URL: /estudiantes/{rut}

Ejemplo: /estudiantes/12345678-9

🔹 Crear un nuevo estudiante
Método: POST

URL: /estudiantes

Body (JSON):
{
  "rut": "11111111-1",
  "nombre": "Carlos Soto",
  "edad": 18,
  "curso": "4° Medio"
}

📗 Evaluacion Service – http://localhost:8002
🔹 Obtener todas las evaluaciones
Método: GET

URL: /evaluaciones

🔹 Obtener una evaluación por ID
Método: GET

URL: /evaluaciones/{id}

Ejemplo: /evaluaciones/eval-001

🔹 Crear una nueva evaluación
Método: POST

URL: /evaluaciones

Body (JSON):

{
  "id": "eval-003",
  "rut_estudiante": "12345678-9",
  "semestre": "2° Semestre 2025",
  "asignatura": "Física",
  "evaluacion": 7.0
}
