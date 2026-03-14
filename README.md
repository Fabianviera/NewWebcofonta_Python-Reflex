# COFONTA® — Web en Python + Reflex

Sitio web completo de **COFONTA, S.L.** desarrollado con [Reflex](https://reflex.dev), el framework Python full-stack que compila a React + FastAPI.

---

## Estructura del proyecto

```
cofonta_reflex/
├── rxconfig.py                  # Configuración de Reflex
├── requirements.txt
├── assets/
│   ├── images/
│   │   ├── logo_cofonta.png     # Logo blanco con fondo transparente
│   │   ├── foto_administracion.jpg
│   │   ├── foto_tienda.jpg
│   │   ├── obra_auditorio.jpg
│   │   └── ...
│   └── curriculum_cofonta.pdf
└── cofonta/
    ├── __init__.py              # App principal + registro de páginas
    ├── styles.py                # Paleta, tipografía y estilos globales
    ├── components/
    │   ├── __init__.py
    │   ├── navbar.py            # Barra de navegación
    │   └── footer.py           # Pie de página
    └── pages/
        ├── __init__.py
        ├── index.py             # Página principal (una sola página con anclas)
        ├── legal.py             # Aviso legal, privacidad, cookies, calidad
        └── mapas.py             # Mapas de oficina, almacén y tienda
```

---

## Páginas incluidas

| Ruta                   | Descripción                        |
|------------------------|------------------------------------|
| `/`                    | Página principal (hero, servicios, empresa, obras, tienda, contacto) |
| `/aviso-legal`         | Aviso Legal (LSSI-CE art.10)       |
| `/politica-privacidad` | Política de Privacidad (RGPD)      |
| `/politica-cookies`    | Política de Cookies (ePrivacy)     |
| `/politica-calidad`    | Política de Calidad + PRL          |
| `/mapa-oficina`        | Mapa oficina de administración     |
| `/mapa-almacen`        | Mapa almacén central               |
| `/mapa-tienda`         | Mapa tienda El Sauzal              |

---

## Requisitos

- Python 3.9 o superior
- Node.js 18 o superior (lo necesita Reflex internamente)

---

## Instalación y puesta en marcha

```bash
# 1. Clonar o descomprimir el proyecto
cd cofonta_reflex

# 2. Crear entorno virtual (recomendado)
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Inicializar Reflex (solo la primera vez)
reflex init

# 5. Arrancar en modo desarrollo
reflex run
```

La web estará disponible en **http://localhost:3000**

---

## Producción

```bash
# Compilar para producción
reflex export --frontend-only

# O desplegar con el backend incluido
reflex run --env prod
```

Para despliegue en servidor recomendamos usar **[Reflex Cloud](https://reflex.dev/docs/hosting/deploy-quick-start/)** o un VPS con Nginx + systemd.

---

## Personalización

- **Colores y fuentes** → `cofonta/styles.py`
- **Textos y contenido** → `cofonta/pages/index.py`
- **Navegación** → `cofonta/components/navbar.py`
- **Pie de página** → `cofonta/components/footer.py`
- **Imágenes** → carpeta `assets/images/`

---

Desarrollado por **Fabián Viera**
