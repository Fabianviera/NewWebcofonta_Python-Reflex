# Guía de contribución

¡Gracias por tu interés en contribuir a **COFONTA Web**! A continuación encontrarás las pautas para hacerlo de forma ordenada.

---

## Flujo de trabajo

1. **Crea un fork** del repositorio en tu cuenta de GitHub.
2. **Clona** tu fork localmente:
   ```bash
   git clone https://github.com/<tu-usuario>/NewWebcofonta_Python-Reflex.git
   cd NewWebcofonta_Python-Reflex
   ```
3. **Crea una rama** con un nombre descriptivo:
   ```bash
   git checkout -b feat/nombre-de-la-feature
   # o
   git checkout -b fix/descripcion-del-bug
   ```
4. **Realiza tus cambios** siguiendo las convenciones del proyecto.
5. **Comprueba el linter** antes de hacer commit:
   ```bash
   pip install ruff
   ruff check .
   ```
6. **Haz commit** con mensajes claros. Usa prefijos en inglés ([Conventional Commits](https://www.conventionalcommits.org/)) y descripción en español o inglés:
   ```bash
   git commit -m "feat: add testimonios section to homepage"
   # o en español:
   git commit -m "feat: añade sección de testimonios en la página principal"
   ```
7. **Haz push** a tu fork y abre un **Pull Request** contra la rama `main`.

---

## Convenciones de código

- Código Python formateado según **PEP 8** (validado con `ruff`).
- Nombres de variables y funciones en **snake_case**.
- Comentarios de sección en español, siguiendo el estilo del código existente.
- Estilos y colores centralizados en `cofonta/styles.py` — no uses valores mágicos dispersos.

---

## Estructura de ramas

| Rama | Uso |
|------|-----|
| `main` | Producción — solo merges mediante PR revisado |
| `develop` | Integración de features en curso |
| `feat/*` | Nuevas funcionalidades |
| `fix/*` | Corrección de errores |
| `docs/*` | Cambios solo de documentación |

---

## Entorno de desarrollo

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# Instalar dependencias + herramientas de desarrollo
pip install -r requirements.txt
pip install ruff

# Arrancar en modo desarrollo
reflex run
```

---

## Reporte de bugs

Abre un [issue](https://github.com/Fabianviera/NewWebcofonta_Python-Reflex/issues) con:

- Descripción clara del problema.
- Pasos para reproducirlo.
- Versión de Python y sistema operativo.
- Captura de pantalla o log de error (si aplica).

---

Desarrollado por **Fabián Viera** · [COFONTA, S.L.](https://cofonta.es)
