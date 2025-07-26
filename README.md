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


## Pasos para ejecutar la aplicación localmente:
### 1. **Aplicar migraciones de base de datos**
Dado que se trata de una configuración nueva, necesita crear la base de datos y aplicar las migraciones:
``` bash
# Crear y aplicar las migraciones iniciales
python manage.py makemigrations

# Aplicar las migraciones para crear las tablas de la base de datos
python manage.py migrate
```
### 2. **Crear un superusuario**
Crear un usuario administrador para acceder a la interfaz de administración de Django:
``` bash
python manage.py createsuperuser
```
Se le pedirá que ingrese:
- Nombre de usuario
- Correo electrónico (opcional)
- Contraseña (ingrésela dos veces para confirmar)

### 3. **Recopilar archivos estáticos** (si es necesario)
Dado que está usando Whitenoise para los archivos estáticos, recopílelos:
``` bash
python manage.py collectstatic
```
### 4. **Ejecutar el servidor de desarrollo**
Iniciar El servidor de desarrollo de Django:
``` bash
python manage.py runserver
```
De forma predeterminada, esto iniciará el servidor en `http://127.0.0.1:8000/` o `http://localhost:8000/`
