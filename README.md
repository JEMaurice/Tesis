
## 📌 Proyecto

Aplicación web para la gestión de fichas técnicas en una empresa textil. El sistema centraliza la información necesaria para la fabricación y logística del producto, permitiendo a cada sector (administración, corte, estampado, avíos, confección y control de calidad) acceder a la información y materiales relacionados con cada ficha técnica.

Características principales:

- Gestión completa de fichas técnicas (crear, editar, estados, imágenes y observaciones por sector).
- Administración de clientes, prototipos e insumos.
- Chat en tiempo real por salas (implementado con Django Channels) para comunicación entre sectores.
- Calculador básico de materia prima para estimar recursos necesarios.
- Gestión de usuarios con modelo de usuario personalizado y asignación por sector.

## 🧩 Estructura y apps principales

El proyecto utiliza Django y está organizado en aplicaciones dentro de `applications/`. Las apps incluidas son (entre otras):

- `home` — vistas principales y autenticación.
- `cliente` — gestión de clientes.
- `ficha_tecnica` — modelo y vistas de ficha técnica (imágenes, observaciones por sector, estados).
- `insumo` — gestión de insumos.
- `prototipo` — gestión de prototipos.
- `proveedor` — agenda/gestión de proveedores.
- `sector` — definición de sectores y relaciones.
- `usuario` — modelo de usuario personalizado (`AUTH_USER_MODEL = 'usuario.Usuarios'`).
- `mensajeria` — chat en tiempo real (WebSocket consumer en `applications/mensajeria/consumers.py`).

## 📦 Dependencias principales

Las dependencias se listan en `requirements.txt`. Entre las más importantes:

- Django >= 4.2
- channels, daphne, channels-redis (para chat en tiempo real)
- django-ckeditor
- Pillow
- psycopg2-binary (PostgreSQL)

## ⚙️ Configuración y ejecución (desarrollo)

1. Crear y activar un entorno virtual (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

3. Configurar la base de datos y secretos:

- El archivo de configuración por defecto para desarrollo es `test_project/settings/local.py`. Por defecto usa PostgreSQL y valores de ejemplo (`db_tesis`, usuario `admin`). Puedes crear un `secret.json` en la raíz del repo para sobrescribir `SECRET_KEY` y credenciales de la base de datos. Ejemplo mínimo de `secret.json`:

```json
{
	"SECRET_KEY": "tu_clave_secreta",
	"DB_NAME": "nombre_bd",
	"USER": "usuario",
	"PASSWORD": "contraseña"
}
```

4. Crear migraciones y aplicar migraciones:

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Crear un superusuario (opcional):

```powershell
python manage.py createsuperuser
```

6. Ejecutar servidor de desarrollo:

```powershell
python manage.py runserver
```

Nota sobre chat en tiempo real: `applications.mensajeria` usa Django Channels y requiere un broker (la configuración por defecto en `base.py` usa Redis en `localhost:6379`). Asegúrate de tener Redis corriendo para que el chat funcione correctamente. En producción se recomienda usar `daphne` o `uvicorn` y un proceso de canal layers con Redis.

Ejemplo para correr con `daphne`:

```powershell
daphne -b 0.0.0.0 -p 8000 test_project.asgi:application
```

## 📚 Documentación

- [01Diagramas](Documentacion/01Diagramas/)  
	- Diagramas del proyecto: mapas de flujo, diagramas de casos de uso y arquitectura.

- [02Bocetodevistas](Documentacion/02Bocetodevistas/)  
	- Bocetos y maquetas de las vistas principales del sistema.

- [03Trabajofinal](Documentacion/03Trabajofinal/)  
	- Trabajo final: documento con la memoria del proyecto y entregables finales.

## ✅ Estado y recomendaciones

- Estado actual: aplicación con estructura completa, modelo de ficha técnica y chat en tiempo real implementados.
- Recomendaciones antes de desplegar en producción:
	- Configurar correctamente `SECRET_KEY` y credenciales de la base de datos en `secret.json` o variables de entorno.
	- Asegurar que Redis esté disponible para Channels y configurar `CHANNEL_LAYERS` para producción.
	- Ajustar `ALLOWED_HOSTS`, `DEBUG=False` y parámetros de seguridad.

