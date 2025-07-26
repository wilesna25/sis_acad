### Resumen del proyecto
Este es un sistema de gestión académica basado en Django que gestiona:
- Matrícula y gestión de estudiantes
- Gestión de cursos/asignaturas
- Seguimiento de calificaciones y asistencia
- Gestión de periodos académicos
- Gestión del profesorado
- Gestión de campus/ubicaciones

### Modelos clave
1. Estudiantes
2. Profesores - Extiende el AbstractUser de Django, Docentes
3. Asignaturas
4. Grupos
5. Matrículas
6. Calificaciones
7. Periodo académico


En el archivo `requirements.txt` incluye:
1. **Dependencias principales**: Django 3.1.7 (compatible con la versión settings.py)
2. **Archivos estáticos**: whitenoise (ya utilizado en middleware)
3. **Producción**: gunicorn para servir la aplicación
4. **Utilidades**: Paquetes comunes útiles para un sistema de gestión académica
5. **Características opcionales**: Paquetes para posibles mejoras futuras, como la gestión de imágenes, la exportación a Excel y los informes en PDF

El archivo está estructurado para ser compatible con entornos de desarrollo y producción. Es posible que desee crear archivos de requisitos separados (`requirements-dev.txt`, `requirements-prod.txt`) a medida que el proyecto crezca.
