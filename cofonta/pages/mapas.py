"""Páginas de mapas: Oficina, Almacén y Tienda."""
import reflex as rx
from cofonta.styles import (
    NAVY, STEEL, SKY, WATER, WHITE, GOLD, MUTED, TEXT,
    FONT_HEADING, FONT_BODY, FONT_SERIF,
)
from cofonta.components import navbar, footer

GOOGLE_FONTS = "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap"


def mapa_shell(
    eyebrow_text: str,
    title: str,
    italic: str,
    map_src: str,
    directions_href: str,
    back_href: str,
    back_label: str,
    info_title: str,
    address: str,
    tel: str,
    email: str,
) -> rx.Component:
    return rx.box(
        rx.el.link(rel="stylesheet", href=GOOGLE_FONTS),
        navbar(),
        # Hero
        rx.box(
            rx.hstack(
                rx.box(width="30px", height="1px", background=GOLD),
                rx.text(eyebrow_text, font_family=FONT_BODY, font_size="0.7rem",
                        letter_spacing="0.25em", text_transform="uppercase", color=GOLD),
                align="center", gap="1rem", margin_bottom="0.8rem",
            ),
            rx.heading(
                title,
                rx.text.span(italic, font_family=FONT_SERIF, font_style="italic", color=WATER),
                font_family=FONT_HEADING,
                font_size="3.2rem",
                letter_spacing="0.05em", color=WHITE, line_height="1",
                as_="h1",
            ),
            padding="9rem 3rem 3rem",
            background=f"linear-gradient(160deg, {NAVY} 0%, #0d2040 100%)",
            border_bottom="1px solid rgba(59,130,196,0.1)",
            width="100%",
        ),
        # Cuerpo: mapa + panel
        rx.flex(
            # Mapa
            rx.box(
                rx.el.iframe(
                    src=map_src,
                    width="100%",
                    height="500px",
                    style={"border": "none", "display": "block"},
                    allow_full_screen=True,
                    loading="lazy",
                ),
                border="1px solid rgba(59,130,196,0.2)",
                overflow="hidden",
                flex="1",
                min_width="0",
            ),
            # Panel info
            rx.vstack(
                # Tarjeta de datos
                rx.box(
                    rx.hstack(
                        rx.box(width="16px", height="1px", background=GOLD),
                        rx.text(info_title, font_family=FONT_BODY, font_size="0.68rem",
                                letter_spacing="0.22em", text_transform="uppercase", color=GOLD),
                        align="center", gap="0.6rem", margin_bottom="1.2rem",
                    ),
                    rx.hstack(
                        rx.text("📍", font_size="0.9rem", color=SKY, min_width="18px"),
                        rx.text(address, font_family=FONT_BODY, font_weight="300",
                                color=MUTED, font_size="0.88rem", line_height="1.65"),
                        align="start", gap="0.9rem", margin_bottom="0.85rem",
                    ),
                    rx.hstack(
                        rx.text("📞", font_size="0.9rem", color=SKY, min_width="18px"),
                        rx.text(tel, font_family=FONT_BODY, font_weight="300",
                                color=MUTED, font_size="0.88rem"),
                        align="start", gap="0.9rem", margin_bottom="0.85rem",
                    ),
                    rx.hstack(
                        rx.text("✉️", font_size="0.9rem", color=SKY, min_width="18px"),
                        rx.link(email, href=f"mailto:{email}",
                                font_family=FONT_BODY, font_weight="300",
                                color=MUTED, font_size="0.88rem",
                                text_decoration="none", _hover={"color": WATER}),
                        align="start", gap="0.9rem",
                    ),
                    padding="1.8rem",
                    background=STEEL,
                    border="1px solid rgba(59,130,196,0.15)",
                    width="100%",
                ),
                # Botón cómo llegar
                rx.link(
                    "📍  Cómo llegar (Google Maps)",
                    href=directions_href,
                    target="_blank",
                    rel="noopener",
                    font_family=FONT_BODY,
                    font_size="0.8rem",
                    letter_spacing="0.1em",
                    text_transform="uppercase",
                    padding="0.9rem 1.6rem",
                    background=SKY,
                    color=WHITE,
                    text_decoration="none",
                    display="block",
                    text_align="center",
                    transition="background 0.25s",
                    _hover={"background": WATER, "color": NAVY},
                    width="100%",
                ),
                # Botón volver
                rx.link(
                    f"← {back_label}",
                    href=back_href,
                    font_family=FONT_BODY,
                    font_size="0.8rem",
                    letter_spacing="0.1em",
                    text_transform="uppercase",
                    padding="0.9rem 1.6rem",
                    background="transparent",
                    color=MUTED,
                    text_decoration="none",
                    display="block",
                    text_align="center",
                    border="1px solid rgba(139,175,200,0.3)",
                    transition="all 0.25s",
                    _hover={"border_color": MUTED, "color": WHITE},
                    width="100%",
                ),
                gap="1.5rem",
                width="340px",
                flex_shrink="0",
                align="stretch",
            ),
            direction="row",
            gap="3rem",
            align="start",
            padding="3rem 3rem",
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        footer(),
        background=NAVY, font_family=FONT_BODY, color=TEXT,
        width="100%", overflow_x="hidden",
        min_height="100vh",
        display="flex",
        flex_direction="column",
    )


@rx.page(route="/mapa-oficina", title="Ubicación Oficina — COFONTA®")
def mapa_oficina() -> rx.Component:
    return mapa_shell(
        eyebrow_text="Ubicación",
        title="Oficina de ",
        italic="Administración",
        map_src="https://maps.google.com/maps?q=Calle+Las+Higueras+8,+38350+Tacoronte,+Tenerife&output=embed&z=17&hl=es",
        directions_href="https://maps.google.com/maps/dir//Calle+Las+Higueras+8,+38350+Tacoronte,+Tenerife",
        back_href="/#contacto",
        back_label="Volver a Contacto",
        info_title="Administración — Tacoronte",
        address="Calle Las Higueras, n.º 8, Local 4\nEdif. Alicia II\n38350 Tacoronte (Tenerife)",
        tel="922 563 501 / 717 793 246",
        email="cofonta-oficina@cofonta.com",
    )


@rx.page(route="/mapa-almacen", title="Ubicación Almacén — COFONTA®")
def mapa_almacen() -> rx.Component:
    return mapa_shell(
        eyebrow_text="Ubicación",
        title="Almacén ",
        italic="Central",
        map_src="https://maps.google.com/maps?q=Calle+La+Cuesta+4B,+38350+Tacoronte,+Tenerife&output=embed&z=17&hl=es",
        directions_href="https://maps.google.com/maps/dir//Calle+La+Cuesta+4B,+38350+Tacoronte,+Tenerife",
        back_href="/#contacto",
        back_label="Volver a Contacto",
        info_title="Almacén Central — Tacoronte",
        address="Calle La Cuesta, 4B\nEdif. Cofonta I\n38350 Tacoronte (Tenerife)",
        tel="922 571 770",
        email="cofonta-almacen@cofonta.com",
    )


@rx.page(route="/mapa-tienda", title="Ubicación Tienda El Sauzal — COFONTA®")
def mapa_tienda() -> rx.Component:
    return mapa_shell(
        eyebrow_text="Ubicación",
        title="Tienda ",
        italic="El Sauzal",
        map_src="https://maps.google.com/maps?q=TF-152+8,+38360+El+Sauzal,+Tenerife&output=embed&z=16&hl=es",
        directions_href="https://maps.google.com/maps/dir//Ctra.+General+del+Norte+TF-152+8,+38360+El+Sauzal,+Tenerife",
        back_href="/#tienda",
        back_label="Volver a Tienda",
        info_title="Tienda — El Sauzal",
        address="Ctra. General del Norte TF-152, n.º 8, Local 1\n38360 El Sauzal (Tenerife)",
        tel="922 561 142",
        email="tienda@cofonta.com",
    )
