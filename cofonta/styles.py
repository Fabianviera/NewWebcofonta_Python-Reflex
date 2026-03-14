"""
Estilos y variables de diseño globales de COFONTA.
"""

# ── Paleta de colores ──────────────────────────────────────────────────────────
NAVY   = "#0a1628"
STEEL  = "#1c3452"
BLUE   = "#1a56a0"
SKY    = "#3b82c4"
WATER  = "#7eb8d4"
ICE    = "#d4eaf7"
WHITE  = "#f5f9fc"
GOLD   = "#c9a84c"
MUTED  = "#8aafc8"
TEXT   = "#e8f0f7"

# ── Tipografía ─────────────────────────────────────────────────────────────────
FONT_HEADING = "Bebas Neue"
FONT_BODY    = "DM Sans"
FONT_SERIF   = "DM Serif Display"

GOOGLE_FONTS = "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap"

# ── Estilos base para rx.text ──────────────────────────────────────────────────
body_text = dict(
    font_family=FONT_BODY,
    font_weight="300",
    color=MUTED,
    line_height="1.85",
    font_size="0.92rem",
)

muted_label = dict(
    font_family=FONT_BODY,
    font_size="0.7rem",
    letter_spacing="0.25em",
    text_transform="uppercase",
    color=GOLD,
)

heading_bebas = dict(
    font_family=FONT_HEADING,
    letter_spacing="0.05em",
    color=WHITE,
    line_height="1",
)

# ── Estilos de sección ─────────────────────────────────────────────────────────
section_style = dict(
    padding="7rem 3rem",
    width="100%",
)

card_style = dict(
    background=STEEL,
    border=f"1px solid rgba(59,130,196,0.15)",
    padding="2rem",
    transition="all 0.3s",
)

# ── Botones ────────────────────────────────────────────────────────────────────
btn_primary = dict(
    background=BLUE,
    color=WHITE,
    font_family=FONT_BODY,
    font_size="0.82rem",
    letter_spacing="0.12em",
    text_transform="uppercase",
    padding="0.9rem 2.2rem",
    border="none",
    cursor="pointer",
    text_decoration="none",
    display="inline-block",
    transition="background 0.25s",
    _hover={"background": SKY},
)

btn_ghost = dict(
    background="transparent",
    color=MUTED,
    font_family=FONT_BODY,
    font_size="0.82rem",
    letter_spacing="0.12em",
    text_transform="uppercase",
    padding="0.9rem 2.2rem",
    border=f"1px solid rgba(139,175,200,0.3)",
    cursor="pointer",
    text_decoration="none",
    display="inline-block",
    transition="all 0.25s",
    _hover={"border_color": MUTED, "color": WHITE},
)

# ── Input / Textarea ───────────────────────────────────────────────────────────
input_style = dict(
    width="100%",
    padding="0.9rem 1rem",
    background="rgba(10,22,40,0.6)",
    border=f"1px solid rgba(59,130,196,0.2)",
    color=WHITE,
    font_family=FONT_BODY,
    font_size="0.9rem",
    outline="none",
    _focus={"border_color": SKY},
    _placeholder={"color": MUTED},
)
