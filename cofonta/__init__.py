"""Aplicación web COFONTA, S.L. construida con Reflex."""
import reflex as rx

# Importar todas las páginas para que Reflex las registre
from cofonta.pages import (
    index,
    aviso_legal,
    politica_privacidad,
    politica_cookies,
    politica_calidad,
    mapa_oficina,
    mapa_almacen,
    mapa_tienda,
)

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap",
    ],
    style={
        "box_sizing": "border-box",
        "margin": "0",
        "padding": "0",
        "scroll_behavior": "smooth",
        "*": {"box_sizing": "border-box"},
    },
)
