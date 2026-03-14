"""Componente de navegación compartido."""
import reflex as rx
from cofonta.styles import (
    NAVY, SKY, GOLD, MUTED, WHITE, FONT_HEADING, FONT_BODY
)


def nav_logo() -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.image(
                src="/images/logo_cofonta.png",
                height="42px",
                width="auto",
            ),
            rx.text(
                "COFONTA",
                font_family=FONT_HEADING,
                font_size="2rem",
                letter_spacing="0.12em",
                color=WHITE,
            ),
            rx.text(
                "®",
                font_size="0.75rem",
                color=GOLD,
                vertical_align="super",
                margin_top="-0.8rem",
            ),
            align="center",
            gap="0.7rem",
        ),
        href="/",
        text_decoration="none",
        _hover={"text_decoration": "none"},
    )


def nav_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        font_family=FONT_BODY,
        font_size="0.8rem",
        letter_spacing="0.12em",
        text_transform="uppercase",
        color=MUTED,
        text_decoration="none",
        _hover={"color": WHITE},
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            nav_logo(),
            # Links desktop (ocultos en móvil)
            rx.hstack(
                nav_link("Inicio", "/"),
                nav_link("La Empresa", "/#empresa"),
                nav_link("Obras", "/#obras"),
                nav_link("Tienda", "/#tienda"),
                nav_link("Contacto", "/#contacto"),
                gap="2.5rem",
                display=["none", "none", "flex"],
            ),
            rx.link(
                "Solicitar presupuesto",
                href="/#contacto",
                font_family=FONT_BODY,
                font_size="0.78rem",
                letter_spacing="0.1em",
                text_transform="uppercase",
                padding="0.55rem 1.4rem",
                border=f"1px solid {SKY}",
                color=SKY,
                text_decoration="none",
                background="transparent",
                transition="all 0.25s",
                _hover={"background": SKY, "color": NAVY},
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="100",
        padding=["1rem 1.5rem", "1rem 1.5rem", "1.2rem 3rem"],
        background="rgba(10,22,40,0.9)",
        backdrop_filter="blur(12px)",
        border_bottom="1px solid rgba(59,130,196,0.15)",
    )
