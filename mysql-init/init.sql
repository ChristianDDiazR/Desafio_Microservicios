CREATE TABLE IF NOT EXISTS estudiantes (
    rut VARCHAR(12) PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    curso VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS evaluaciones (
    id VARCHAR(50) PRIMARY KEY,
    rut_estudiante VARCHAR(12),
    semestre VARCHAR(20),
    asignatura VARCHAR(100),
    evaluacion FLOAT,
    FOREIGN KEY (rut_estudiante) REFERENCES estudiantes(rut)
);

INSERT INTO estudiantes (rut, nombre, edad, curso) VALUES
('12345678-9', 'Juan Pérez', 17, '4° Medio'),
('98765432-1', 'María González', 16, '3° Medio');

INSERT INTO evaluaciones (id, rut_estudiante, semestre, asignatura, evaluacion) VALUES
('eval-001', '12345678-9', '1° Semestre 2025', 'Matemáticas', 6.5),
('eval-002', '98765432-1', '1° Semestre 2025', 'Historia', 5.8);
