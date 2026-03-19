# Contribuir a NewWebcofonta_Python-Reflex

¡Gracias por tu interés en contribuir! Este documento explica cómo puedes colaborar en el proyecto.

---

## Cómo contribuir

### 1. Haz un fork y clona el repositorio

```bash
git clone https://github.com/<tu-usuario>/NewWebcofonta_Python-Reflex.git
cd NewWebcofonta_Python-Reflex
```

### 2. Crea un entorno virtual e instala dependencias

```bash
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

pip install -r requirements.txt
pip install ruff                 # herramienta de linting / formateo
```

### 3. Crea una rama para tu cambio

```bash
git checkout -b feature/nombre-descriptivo
```

Usa prefijos descriptivos como:

| Prefijo    | Cuándo usarlo                              |
|------------|--------------------------------------------|
| `feature/` | Nueva funcionalidad                        |
| `fix/`     | Corrección de un error                     |
| `docs/`    | Solo cambios en documentación              |
| `refactor/`| Refactorización sin cambio de funcionalidad|
| `chore/`   | Tareas de mantenimiento (deps, CI, etc.)   |

### 4. Comprueba el estilo antes de hacer commit

El proyecto usa **ruff** para lint y formateo:

```bash
# Comprobar errores de lint
ruff check .

# Aplicar autoformato
ruff format .
```

Todos los archivos deben superar estas comprobaciones antes de abrir un PR, ya que el workflow de CI las ejecutará automáticamente.

### 5. Abre un Pull Request

- Dirígete a tu fork en GitHub y pulsa **"Compare & pull request"**.
- Describe brevemente qué cambia y por qué.
- El PR se revisa manualmente y debe pasar el **workflow de CI** (lint + comprobación de sintaxis).

---

## Estilo de código

- Sigue **PEP 8** (ruff lo comprueba automáticamente).
- Usa nombres de variables y funciones en **inglés** o en **español** de forma coherente con el resto del archivo.
- Mantén las líneas por debajo de **100 caracteres** siempre que sea posible.
- Escribe **docstrings** en los módulos, clases y funciones públicas.

---

## Estructura del proyecto

```
cofonta/
├── __init__.py          # App principal + registro de páginas
├── cofonta.py           # Punto de entrada esperado por Reflex
├── styles.py            # Paleta, tipografía y estilos globales
├── components/
│   ├── navbar.py        # Barra de navegación
│   └── footer.py        # Pie de página
└── pages/
    ├── index.py         # Página principal
    ├── legal.py         # Páginas legales
    └── mapas.py         # Mapas de ubicaciones
```

---

## Reportar un bug

Si encuentras un bug, abre un **Issue** en GitHub con:

1. Una descripción clara del problema.
2. Pasos para reproducirlo.
3. Comportamiento esperado vs. comportamiento real.
4. Versión de Python y sistema operativo.

---

Desarrollado por **Fabián Viera**
