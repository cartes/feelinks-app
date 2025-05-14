# Feelinks.app

Feelinks.app es un sistema tipo Linktree desarrollado en Python con Django, utilizando Tailwind CSS y Flowbite para la interfaz. Permite a los usuarios crear y personalizar una página pública con enlaces, colores y opciones visuales de manera sencilla y rápida.

## Tecnologías principales

* **Backend:** Django (monolítico)
* **Frontend:** Django Templates + Tailwind CSS + Flowbite
* **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)
* **Componentes:**

  * Flowbite (componentes Tailwind)
  * Google Fonts (Inter, Poppins, Raleway)
  * FontAwesome (opcional)

## Requisitos

* Python >= 3.10
* Django >= 4.2
* Node.js y npm (para compilar Tailwind con PostCSS y Flowbite)

## Instalación local

```bash
# Clonar el repositorio
https://github.com/cartes/feelinks-app.git
cd feelinks-app

# Crear y activar entorno virtual
python -m venv env
source env/bin/activate  # o "env\Scripts\activate" en Windows

# Instalar dependencias
pip install -r requirements.txt

# Instalar dependencias frontend
npm install
npm run dev  # para compilar Tailwind y ver cambios en caliente

# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Levantar servidor
python manage.py runserver
```

## Estructura del proyecto

```
feelinks-app/
├── dashboard/          # App principal con el dashboard del usuario
├── public/             # Templates y vistas públicas
├── static/             # Archivos estáticos compilados (JS/CSS)
├── templates/          # Base templates HTML
├── tailwind.config.js  # Configuración de Tailwind y Flowbite
├── requirements.txt    # Dependencias Python
├── package.json        # Dependencias JS
├── manage.py
└── README.md
```

## Convenciones sintácticas y estilo de código

### Python (Django)

* Se sigue PEP8 (indentación de 4 espacios)
* Los modelos están en `dashboard/models.py`
* Formularios en `forms.py` están estilizados con clases de Tailwind desde el backend
* Las rutas usan `path()` en lugar de `url()`
* Las vistas se organizan en base a vistas basadas en funciones (FBV)

### HTML + Tailwind

* Se usa la convención de clases utilitarias de Tailwind
* Componentes Flowbite integrados (modales, tabs, dropdowns, etc.)
* Clases personalizadas opcionales usando `@layer` en CSS

### JavaScript

* Se utiliza JS vanilla para interacciones simples (no se usa React)

## Personalización de perfiles

* Cada usuario puede elegir:

  * Colores: fondo, texto, primario
  * Tipografía (Inter, Poppins, Raleway, etc.)
  * Avatar (imagen o letra inicial)
  * Mostrar o no el footer con invitación a Feelinks.app
  * Animaciones en su página

## Autenticación

* Basada en el sistema por defecto de Django (`User` model extendido con `Profile`)
* Se usa `django.contrib.auth` para login/logout

## Estado actual

* [x] Sistema de registro e inicio de sesión personalizado
* [x] Dashboard funcional con sidebar tipo App Shell
* [x] Sistema de perfiles con campos visuales
* [x] Compilación de estilos con Tailwind + Flowbite
* [x] Homepage pública disponible
* [ ] Paso a paso de onboarding tras registro (próximamente)
* [ ] API pública para enlaces (próximamente)

---

Desarrollado con ❤️ por Cristian Cartes
[https://feelinks.app](https://feelinks.app)
