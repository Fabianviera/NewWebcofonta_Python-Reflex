"""Componente de pie de página compartido."""
import reflex as rx
from cofonta.styles import NAVY, GOLD, MUTED, WHITE, WATER, FONT_HEADING, FONT_BODY


def footer() -> rx.Component:
    return rx.box(
        rx.flex(
            # Logo + nombre
            rx.hstack(
                rx.image(src="/images/logo_cofonta.png", height="34px", width="auto"),
                rx.text(
                    "COFONTA",
                    font_family=FONT_HEADING,
                    font_size="1.2rem",
                    letter_spacing="0.12em",
                    color=WHITE,
                ),
                rx.text("®", font_size="0.7rem", color=GOLD, vertical_align="super", margin_top="-0.5rem"),
                align="center",
                gap="0.6rem",
            ),
            # Copyright + crédito
            rx.text(
                "© 2025 COFONTA, S.L. — Las Higueras, 8 local 4, 38350 Tacoronte, Tenerife (España)  ·  Diseñado por Fabián Viera",
                font_family=FONT_BODY,
                font_size="0.75rem",
                color=MUTED,
                font_weight="300",
            ),
            # Links legales
            rx.hstack(
                rx.link("Aviso Legal",    href="/aviso-legal",         font_family=FONT_BODY, font_size="0.72rem", letter_spacing="0.1em", text_transform="uppercase", color=MUTED, text_decoration="none", _hover={"color": WATER}),
                rx.link("Privacidad",     href="/politica-privacidad",  font_family=FONT_BODY, font_size="0.72rem", letter_spacing="0.1em", text_transform="uppercase", color=MUTED, text_decoration="none", _hover={"color": WATER}),
                rx.link("Cookies",        href="/politica-cookies",     font_family=FONT_BODY, font_size="0.72rem", letter_spacing="0.1em", text_transform="uppercase", color=MUTED, text_decoration="none", _hover={"color": WATER}),
                rx.link("Calidad",        href="/politica-calidad",     font_family=FONT_BODY, font_size="0.72rem", letter_spacing="0.1em", text_transform="uppercase", color=MUTED, text_decoration="none", _hover={"color": WATER}),
                gap="1.5rem",
                flex_wrap="wrap",
            ),
            direction="row",
            align="center",
            justify="between",
            wrap="wrap",
            gap="1rem",
            width="100%",
        ),
        padding=["1.5rem", "1.5rem", "2rem 3rem"],
        background=NAVY,
        border_top="1px solid rgba(59,130,196,0.1)",
        width="100%",
    )
