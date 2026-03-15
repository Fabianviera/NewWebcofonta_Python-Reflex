"""Página principal de COFONTA."""
import reflex as rx
from cofonta.styles import (
    NAVY, STEEL, BLUE, SKY, WATER, WHITE, GOLD, MUTED, TEXT,
    FONT_HEADING, FONT_BODY, FONT_SERIF,
    btn_primary, btn_ghost, input_style,
)
from cofonta.components import navbar, footer


# ── Estado del formulario ──────────────────────────────────────────────────────
class ContactState(rx.State):
    nombre:   str = ""
    telefono: str = ""
    email:    str = ""
    servicio: str = ""
    mensaje:  str = ""
    enviado:  bool = False
    error:    str = ""

    def enviar(self):
        if not self.nombre.strip() and not self.mensaje.strip():
            self.error = "Por favor, rellene al menos su nombre y la descripción del proyecto."
            return
        self.error = ""
        self.enviado = True

    def reset_form(self):
        self.nombre = self.telefono = self.email = self.servicio = self.mensaje = ""
        self.enviado = False
        self.error = ""


# ── Helpers de UI ──────────────────────────────────────────────────────────────
def eyebrow(text: str) -> rx.Component:
    return rx.hstack(
        rx.box(width="30px", height="1px", background=GOLD),
        rx.text(text, font_family=FONT_BODY, font_size="0.7rem",
                letter_spacing="0.25em", text_transform="uppercase", color=GOLD),
        align="center", gap="1rem", margin_bottom="1rem",
    )


def section_title(normal: str, italic: str = "") -> rx.Component:
    return rx.heading(
        normal,
        rx.text.span(italic, font_family=FONT_SERIF, font_style="italic", color=WATER)
        if italic else rx.fragment(),
        font_family=FONT_HEADING,
        font_size="4rem",
        letter_spacing="0.05em",
        color=WHITE,
        line_height="1",
        as_="h2",
    )


def stat_block(num: str, suffix: str, label: str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(num,    font_family=FONT_HEADING, font_size="3rem", color=WHITE, line_height="1"),
            rx.text(suffix, font_family=FONT_HEADING, font_size="3rem", color=GOLD,  line_height="1"),
            gap="0",
        ),
        rx.text(label, font_family=FONT_BODY, font_size="0.7rem",
                letter_spacing="0.18em", text_transform="uppercase", color=MUTED),
        align="end", gap="0.2rem",
    )


def service_card(icon_path: str, title: str, desc: str) -> rx.Component:
    return rx.box(
        rx.image(src=icon_path, height="44px", width="44px", margin_bottom="1.5rem"),
        rx.text(title, font_family=FONT_BODY, font_weight="500",
                color=WHITE, font_size="1rem", margin_bottom="0.6rem"),
        rx.text(desc,  font_family=FONT_BODY, font_weight="300",
                color=MUTED, font_size="0.85rem", line_height="1.6"),
        background=STEEL,
        padding="2.5rem",
        border="1px solid transparent",
        transition="all 0.3s",
        _hover={"border_color": f"rgba(59,130,196,0.3)", "background": "#243d5e"},
        position="relative",
    )


def obra_card(img: str, title: str, subtitle: str) -> rx.Component:
    return rx.box(
        rx.image(src=img, width="100%", height="200px", object_fit="cover", display="block"),
        rx.box(
            rx.text(title,    font_family=FONT_BODY, font_weight="500", color=WHITE,
                    font_size="0.9rem", margin_bottom="0.3rem"),
            rx.text(subtitle, font_family=FONT_BODY, font_weight="300", color=MUTED,
                    font_size="0.78rem"),
            padding="1.2rem 1.4rem",
        ),
        background=NAVY,
        border="1px solid rgba(59,130,196,0.12)",
        overflow="hidden",
        transition="transform 0.3s, border-color 0.3s",
        _hover={"transform": "translateY(-4px)", "border_color": "rgba(59,130,196,0.4)"},
    )


def contact_detail(icon: str, content: rx.Component) -> rx.Component:
    return rx.hstack(
        rx.image(src=icon, width="16px", height="16px", flex_shrink="0", margin_top="2px"),
        content,
        align="start", gap="0.9rem", margin_bottom="0.8rem",
    )


def form_field(label: str, component: rx.Component) -> rx.Component:
    return rx.vstack(
        rx.text(label, font_family=FONT_BODY, font_size="0.68rem",
                letter_spacing="0.18em", text_transform="uppercase", color=MUTED),
        component,
        align="stretch", gap="0.5rem", width="100%",
    )


# ── Secciones ──────────────────────────────────────────────────────────────────
def hero_section() -> rx.Component:
    return rx.box(
        # Fondo con gradiente y rejilla
        rx.box(
            background=(
                "radial-gradient(ellipse 80% 60% at 60% 40%, rgba(26,86,160,0.25) 0%, transparent 70%),"
                "linear-gradient(160deg, #0a1628 0%, #0d2040 50%, #0a1628 100%)"
            ),
            position="absolute", inset="0",
        ),
        rx.box(
            background_image=(
                "linear-gradient(rgba(59,130,196,0.04) 1px, transparent 1px),"
                "linear-gradient(90deg, rgba(59,130,196,0.04) 1px, transparent 1px)"
            ),
            background_size="60px 60px",
            position="absolute", inset="0",
        ),
        # Contenido
        rx.box(
            eyebrow("Tenerife · Islas Canarias · Desde 1986"),
            rx.heading(
                "Expertos en",
                rx.el.br(),
                rx.text.span("fontanería", font_family=FONT_SERIF, font_style="italic", color=WATER),
                rx.el.br(),
                "& instalaciones",
                font_family=FONT_HEADING,
                font_size="7rem",
                line_height="0.95",
                letter_spacing="0.04em",
                color=WHITE,
                margin_bottom="1.8rem",
                as_="h1",
            ),
            rx.text(
                "Más de 40 años especializados en fontanería, energía solar, climatización de piscinas "
                "e instalaciones de gas en Canarias. Calidad, seguridad y garantía en cada obra.",
                font_family=FONT_BODY, font_weight="300", color=MUTED,
                font_size="1.05rem", line_height="1.7",
                max_width="520px", margin_bottom="3rem",
            ),
            rx.hstack(
                rx.link("Solicitar presupuesto", href="#contacto", **btn_primary),
                rx.link("Ver obras realizadas",  href="#obras",    **btn_ghost),
                gap="1.2rem", flex_wrap="wrap",
            ),
            position="relative", max_width="760px",
        ),
        # Stats (desktop)
        rx.box(
            stat_block("40", "+", "Años de experiencia"),
            stat_block("15K", "+", "Viviendas construidas"),
            stat_block("30", "+",  "Instalaciones en Canarias"),
            position="absolute", right="3rem", bottom="6rem",
            display="flex",
            flex_direction="column", gap="2.5rem", align_items="flex-end",
        ),
        id="inicio",
        min_height="100vh",
        display="flex",
        flex_direction="column",
        justify_content="flex-end",
        padding="0 3rem 6rem",
        position="relative",
        overflow="hidden",
    )


def services_section() -> rx.Component:
    services = [
        ("☀️", "Energía Solar Térmica",
         "Instalación y mantenimiento de sistemas de captación solar para agua caliente y calefacción."),
        ("🏊", "Filtración y Climatización de Piscinas",
         "Sistemas de filtración, depuración y climatización para todo tipo de piscinas."),
        ("💧", "Grupos de Presión y Bombeo",
         "Instalación de equipos de bombeo y grupos de presión residencial, comercial e industrial."),
        ("🔥", "Calentadores, Calderas y Bombas de Calor",
         "Suministro e instalación de toda la gama de equipos de producción de agua caliente sanitaria."),
        ("🚿", "Griferías y Aparatos Sanitarios",
         "Venta e instalación de griferías, cabinas de hidromasaje, jacuzzis y aparatos sanitarios."),
        ("🏠", "Calefacción: Piso Radiante y Radiadores",
         "Diseño e instalación de sistemas de calefacción por piso radiante, radiadores y fancoils."),
        ("⚡", "Instalación de Gas Propano y Butano",
         "Instalación, revisión y mantenimiento de instalaciones de gas. Revisiones reglamentarias."),
        ("🔧", "Fontanería General",
         "Todo tipo de instalaciones de fontanería y saneamiento, reformas, reparaciones y mantenimiento."),
        ("📋", "Asesoramiento y Presupuestos",
         "Asesoramiento técnico personalizado y presupuestos sin compromiso para cualquier instalación."),
    ]
    return rx.box(
        rx.box(
            eyebrow("Nuestros servicios"),
            section_title("Instalación y ", "venta"),
            margin_bottom="4rem",
        ),
        rx.grid(
            *[
                rx.box(
                    rx.text(icon, font_size="2.5rem", margin_bottom="1rem"),
                    rx.text(title, font_family=FONT_BODY, font_weight="500",
                            color=WHITE, font_size="1rem", margin_bottom="0.6rem"),
                    rx.text(desc, font_family=FONT_BODY, font_weight="300",
                            color=MUTED, font_size="0.85rem", line_height="1.6"),
                    background=STEEL,
                    padding="2.5rem",
                    border="1px solid transparent",
                    transition="all 0.3s",
                    _hover={"border_color": "rgba(59,130,196,0.3)", "background": "#243d5e"},
                )
                for icon, title, desc in services
            ],
            columns="3",
            gap="1px",
            background="rgba(59,130,196,0.1)",
        ),
        id="servicios",
        padding="7rem 3rem",
        background=STEEL,
        width="100%",
    )


def empresa_section() -> rx.Component:
    principios = [
        ("01", "Enfoque al cliente — su satisfacción como fin último de la organización."),
        ("02", "Mejora continua — objetivo prioritario y permanente."),
        ("03", "Trabajo en equipo — compromiso personal en la obtención de la calidad."),
        ("04", "Utilización de materiales de primera calidad, homologados y con certificación."),
        ("05", "Implantación de nuevas tecnologías para la mejora de nuestra gestión."),
    ]
    return rx.box(
        rx.flex(
            # Columna texto
            rx.vstack(
                rx.box(
                    eyebrow("La empresa"),
                    section_title("Más de cuatro décadas ", "construyendo Canarias"),
                    margin_bottom="2rem",
                ),
                rx.text(
                    "COFONTA es una empresa especializada en instalaciones de fontanería, saneamiento, "
                    "energía solar e instalación de gas en las Islas Canarias. Con más de 40 años en el "
                    "sector, nos hemos convertido en una de las principales empresas de instalaciones de "
                    "fontanería de ámbito regional.",
                    **{**{"font_family": FONT_BODY, "font_weight": "300", "color": MUTED,
                          "font_size": "0.92rem", "line_height": "1.85", "margin_bottom": "1rem"}},
                ),
                rx.text(
                    "Nos avalan más de 15.000 viviendas construidas, complejos hoteleros, obras públicas "
                    "y un gran número de reformas, siempre persiguiendo la calidad como prioridad absoluta.",
                    font_family=FONT_BODY, font_weight="300", color=MUTED,
                    font_size="0.92rem", line_height="1.85", margin_bottom="2rem",
                ),
                rx.text("Política de calidad — 5 principios",
                        font_family=FONT_BODY, font_size="0.8rem", letter_spacing="0.15em",
                        text_transform="uppercase", color=GOLD, margin_bottom="1rem"),
                rx.vstack(
                    *[
                        rx.hstack(
                            rx.text(num, font_family=FONT_HEADING, font_size="1.8rem",
                                    color="rgba(59,130,196,0.3)", line_height="1", min_width="36px"),
                            rx.text(txt, font_family=FONT_BODY, font_weight="300",
                                    color=MUTED, font_size="0.9rem", line_height="1.6"),
                            align="start", gap="1rem",
                            padding_y="1rem",
                            border_bottom="1px solid rgba(59,130,196,0.1)",
                            width="100%",
                        )
                        for num, txt in principios
                    ],
                    gap="0", width="100%",
                ),
                # Asociaciones
                rx.box(
                    rx.text("Empresa asociada a", font_family=FONT_BODY, font_size="0.68rem",
                            letter_spacing="0.2em", text_transform="uppercase", color=MUTED,
                            margin_bottom="1rem"),
                    rx.hstack(
                        *[
                            rx.box(name, font_family=FONT_BODY, font_size="0.75rem",
                                   font_weight="500", color=MUTED, letter_spacing="0.08em",
                                   padding="0.6rem 1.2rem",
                                   border="1px solid rgba(59,130,196,0.2)")
                            for name in ["FEMETE", "CONAIF", "APIGASTE"]
                        ],
                        gap="1rem", flex_wrap="wrap",
                    ),
                    margin_top="2rem", padding_top="2rem",
                    border_top="1px solid rgba(59,130,196,0.15)",
                ),
                align="stretch", gap="0", width="100%",
            ),
            # Columna imágenes
            rx.vstack(
                rx.box(
                    rx.image(src="/images/foto_administracion.jpg", width="100%",
                             height="260px", object_fit="cover", display="block"),
                    rx.text("Oficina de administración — Tacoronte",
                            font_family=FONT_BODY, font_size="0.72rem",
                            letter_spacing="0.15em", text_transform="uppercase",
                            color=MUTED, padding="0.8rem 1.2rem"),
                    background=STEEL, border="1px solid rgba(59,130,196,0.15)",
                    overflow="hidden", margin_bottom="1.5rem",
                ),
                rx.box(
                    rx.image(src="/images/foto_tienda.jpg", width="100%",
                             height="260px", object_fit="cover", display="block"),
                    rx.text("Tienda — El Sauzal",
                            font_family=FONT_BODY, font_size="0.72rem",
                            letter_spacing="0.15em", text_transform="uppercase",
                            color=MUTED, padding="0.8rem 1.2rem"),
                    background=STEEL, border="1px solid rgba(59,130,196,0.15)",
                    overflow="hidden", margin_left="1.5rem",
                ),
                align="stretch", gap="0",
            ),
            direction="row",
            gap="5rem",
            align="start",
            width="100%",
        ),
        id="empresa",
        padding="7rem 3rem",
        background=NAVY,
        width="100%",
    )


def obras_section() -> rx.Component:
    obras = [
        ("/images/obra_auditorio.jpg",     "Auditorio de Tenerife",        "S/C de Tenerife · Thyssen Ingeniería"),
        ("/images/obra_torre.jpg",         "Torre Uno de S/C de Tenerife", "S/C de Tenerife · Ferrovial Agroman"),
        ("/images/obra_melia.jpg",         "Hotel Meliá Jardines del Teide","Fañabé · El Caobo, S.L."),
        ("/images/obra_atlantida.jpg",     "Hotel Silken Atlántida",        "S/C de Tenerife · Candesa, S.A."),
        ("/images/obra_atlantic_golf.jpg", "Residencial Atlantic Golf",     "San Miguel de Abona · 798 viviendas"),
        ("/images/obra_gabriela.jpg",      "Residencial Gabriela I, II y III","Avda. Los Menceyes, Candelaria"),
    ]
    otras = [
        "Reforma integral Hotel Maritim, Puerto de la Cruz",
        "Centro para Mayores Los Realejos (Nigrocon, S.L.)",
        "Centro para Mayores Santa Úrsula (Nigrocon, S.L.)",
        "Colegio Echey 1, Ofra (Nigrocon, S.L.)",
        "Resd. La Graciosa, Puertito de Güimar · 112 viviendas",
        "Resd. Alegranza, Puertito de Güimar · 104 viviendas",
        "Resd. Roque de Garachico · 122 viviendas",
        "Resd. Elena, Candelaria · 285 viviendas",
        "Edf. Rambla, Candelaria · 212 viviendas",
        "Resd. Carolina, Candelaria · 270 viviendas",
        "300 viviendas VPO La Atalaya, Tacoronte",
        "63 viviendas VPO Polígono El Rosario (OHL)",
    ]
    return rx.box(
        rx.box(
            eyebrow("Portafolio"),
            section_title("Obras de ", "referencia"),
            margin_bottom="4rem",
        ),
        rx.grid(
            *[obra_card(img, t, s) for img, t, s in obras],
            columns="3",
            gap="1.5rem",
            margin_bottom="3rem",
        ),
        rx.text("Más obras realizadas",
                font_family=FONT_BODY, font_size="0.8rem", letter_spacing="0.15em",
                text_transform="uppercase", color=GOLD, margin_bottom="1.5rem"),
        rx.grid(
            *[
                rx.hstack(
                    rx.text("—", color="rgba(59,130,196,0.4)", font_size="0.7rem"),
                    rx.text(o, font_family=FONT_BODY, font_weight="300", color=MUTED, font_size="0.85rem"),
                    align="baseline", gap="0.6rem",
                    padding_y="0.5rem",
                    border_bottom="1px solid rgba(59,130,196,0.07)",
                    width="100%",
                )
                for o in otras
            ],
            columns="2",
            gap="0",
            margin_bottom="2.5rem",
        ),
        rx.link(
            "Descargar Currículum de Empresa (PDF)",
            href="/curriculum_cofonta.pdf",
            **btn_ghost,
        ),
        id="obras",
        padding="7rem 3rem",
        background=f"linear-gradient(180deg, {STEEL} 0%, {NAVY} 100%)",
        width="100%",
    )


def tienda_section() -> rx.Component:
    def info_row_tienda(icon_char: str, content: str) -> rx.Component:
        return rx.hstack(
            rx.text(icon_char, font_size="0.9rem", color=SKY, min_width="18px"),
            rx.text(content, font_family=FONT_BODY, font_weight="300",
                    color=MUTED, font_size="0.88rem", line_height="1.6"),
            align="start", gap="0.8rem", margin_bottom="0.5rem",
        )

    return rx.box(
        rx.flex(
            # Imágenes
            rx.vstack(
                rx.image(src="/images/foto_tienda2.jpg", width="100%",
                         height="240px", object_fit="cover",
                         border="1px solid rgba(59,130,196,0.15)"),
                rx.image(src="/images/foto_tienda3.jpg", width="100%",
                         height="240px", object_fit="cover",
                         border="1px solid rgba(59,130,196,0.15)"),
                gap="1.5rem", width="100%",
            ),
            # Texto
            rx.vstack(
                rx.box(
                    eyebrow("Tienda"),
                    section_title("Materiales y ", "showroom"),
                    margin_bottom="2rem",
                ),
                rx.text(
                    "Nuestra tienda en El Sauzal es un espacio donde podrá ver y elegir entre una amplia "
                    "selección de griferías, aparatos sanitarios, cabinas de hidromasaje, equipos de "
                    "calefacción y todo lo necesario para su instalación.",
                    font_family=FONT_BODY, font_weight="300", color=MUTED,
                    font_size="0.95rem", line_height="1.85", margin_bottom="1.5rem",
                ),
                rx.text(
                    "Nuestro equipo le asesorará para encontrar la solución más adecuada.",
                    font_family=FONT_BODY, font_weight="300", color=MUTED,
                    font_size="0.95rem", line_height="1.85", margin_bottom="1.5rem",
                ),
                rx.box(
                    rx.text("Tienda El Sauzal", font_family=FONT_BODY, font_size="0.7rem",
                            letter_spacing="0.2em", text_transform="uppercase", color=GOLD,
                            margin_bottom="1rem"),
                    info_row_tienda("📍", "Ctra. General del Norte TF-152, 8 Local 1 — 38360 El Sauzal, Tenerife"),
                    info_row_tienda("📞", "922 561 142"),
                    info_row_tienda("✉️", "tienda@cofonta.com"),
                    rx.link("Ver en el mapa →", href="/mapa-tienda",
                            font_family=FONT_BODY, font_size="0.75rem",
                            letter_spacing="0.12em", text_transform="uppercase",
                            color=SKY, text_decoration="none",
                            border_bottom=f"1px solid transparent",
                            padding_bottom="2px",
                            _hover={"border_color": SKY},
                            display="inline-block", margin_top="0.8rem"),
                    padding="1.5rem",
                    border="1px solid rgba(59,130,196,0.15)",
                    background="rgba(28,52,82,0.4)",
                    margin_top="1.5rem",
                ),
                align="stretch", gap="0", width="100%",
            ),
            direction="row",
            gap="5rem",
            align="center",
            width="100%",
        ),
        id="tienda",
        padding="7rem 3rem",
        background=NAVY,
        width="100%",
    )


def contacto_section() -> rx.Component:
    def loc_card(title: str, addr: str, tel: str, email: str, map_href: str) -> rx.Component:
        return rx.box(
            rx.text(title, font_family=FONT_BODY, font_size="0.72rem",
                    letter_spacing="0.2em", text_transform="uppercase",
                    color=GOLD, margin_bottom="1.2rem"),
            rx.hstack(
                rx.text("📍", font_size="0.85rem", color=SKY, min_width="18px"),
                rx.text(addr, font_family=FONT_BODY, font_weight="300",
                        color=MUTED, font_size="0.88rem", line_height="1.6"),
                align="start", gap="0.8rem", margin_bottom="0.7rem",
            ),
            rx.hstack(
                rx.text("📞", font_size="0.85rem", color=SKY, min_width="18px"),
                rx.text(tel, font_family=FONT_BODY, font_weight="300",
                        color=MUTED, font_size="0.88rem"),
                align="start", gap="0.8rem", margin_bottom="0.7rem",
            ),
            rx.hstack(
                rx.text("✉️", font_size="0.85rem", color=SKY, min_width="18px"),
                rx.link(email, href=f"mailto:{email}", font_family=FONT_BODY,
                        font_weight="300", color=MUTED, font_size="0.88rem",
                        text_decoration="none", _hover={"color": WATER}),
                align="start", gap="0.8rem", margin_bottom="0.5rem",
            ),
            rx.link("Ver en el mapa →", href=map_href,
                    font_family=FONT_BODY, font_size="0.75rem",
                    letter_spacing="0.12em", text_transform="uppercase",
                    color=SKY, text_decoration="none", display="inline-block",
                    margin_top="0.8rem",
                    _hover={"color": WATER}),
            padding="2rem",
            border="1px solid rgba(59,130,196,0.15)",
            background="rgba(10,22,40,0.4)",
        )

    return rx.box(
        rx.flex(
            # Columna izquierda — ubicaciones
            rx.vstack(
                rx.box(
                    eyebrow("Contacto"),
                    section_title("Hablemos de", "\nsu proyecto"),
                    margin_bottom="2.5rem",
                ),
                loc_card(
                    "Administración",
                    "Calle Las Higueras, 8 Local 4 - Edif. Alicia II\n38350 Tacoronte (Tenerife)",
                    "922 563 501",
                    "cofonta-oficina@cofonta.com",
                    "/mapa-oficina",
                ),
                rx.box(height="1.5rem"),
                loc_card(
                    "Almacén Central",
                    "Calle La Cuesta 4B - Edif. Cofonta I\n38350 Tacoronte (Tenerife)",
                    "922 571 770",
                    "cofonta-almacen@cofonta.com",
                    "/mapa-almacen",
                ),
                align="stretch", gap="0", width="100%",
            ),
            # Columna derecha — formulario
            rx.vstack(
                rx.text("Solicitar presupuesto",
                        font_family=FONT_HEADING, font_size="2.5rem",
                        letter_spacing="0.05em", color=WHITE, margin_bottom="0.5rem"),
                rx.text("Le responderemos en menos de 24 horas.",
                        font_family=FONT_BODY, font_weight="300", color=MUTED,
                        font_size="0.85rem", margin_bottom="2rem"),
                # Mensaje de éxito
                rx.cond(
                    ContactState.enviado,
                    rx.box(
                        rx.text(
                            "✓ Mensaje preparado. Abra su cliente de correo o escríbanos directamente a cofonta-oficina@cofonta.com",
                            font_family=FONT_BODY, font_size="0.88rem", color=WATER,
                        ),
                        padding="1.2rem",
                        background="rgba(59,130,196,0.12)",
                        border="1px solid rgba(59,130,196,0.4)",
                        margin_bottom="1.5rem",
                        width="100%",
                    ),
                ),
                # Mensaje de error
                rx.cond(
                    ContactState.error != "",
                    rx.box(
                        rx.text(ContactState.error, font_family=FONT_BODY,
                                font_size="0.85rem", color="#e07a5f"),
                        padding="1rem",
                        background="rgba(196,92,59,0.1)",
                        border="1px solid rgba(196,92,59,0.3)",
                        margin_bottom="1rem", width="100%",
                    ),
                ),
                # Campos
                rx.grid(
                    form_field("Nombre",
                        rx.input(placeholder="Su nombre", value=ContactState.nombre,
                                 on_change=ContactState.set_nombre, **input_style)),
                    form_field("Teléfono",
                        rx.input(placeholder="6XX XXX XXX", value=ContactState.telefono,
                                 on_change=ContactState.set_telefono, **input_style)),
                    columns="2", gap="1rem", width="100%",
                ),
                form_field("Email",
                    rx.input(placeholder="correo@ejemplo.com", value=ContactState.email,
                             on_change=ContactState.set_email, **input_style)),
                form_field("Tipo de instalación",
                    rx.input(placeholder="Fontanería, solar, gas...", value=ContactState.servicio,
                             on_change=ContactState.set_servicio, **input_style)),
                form_field("Descripción del proyecto",
                    rx.text_area(placeholder="Cuéntenos en qué podemos ayudarle...",
                                 value=ContactState.mensaje,
                                 on_change=ContactState.set_mensaje,
                                 min_height="120px",
                                 **{k: v for k, v in input_style.items() if k != "font_size"},
                                 font_size="0.9rem")),
                rx.button(
                    "Enviar solicitud →",
                    on_click=ContactState.enviar,
                    width="100%",
                    **{**btn_primary, "padding": "0.9rem"},
                ),
                align="stretch", gap="1.2rem", width="100%",
            ),
            direction="row",
            gap="5rem",
            align="start",
            width="100%",
        ),
        id="contacto",
        padding="7rem 3rem",
        background=STEEL,
        width="100%",
    )


# ── Página completa ────────────────────────────────────────────────────────────
@rx.page(route="/", title="COFONTA® — Instalaciones de Fontanería en Tenerife")
def index() -> rx.Component:
    return rx.box(
        rx.el.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap"),
        navbar(),
        hero_section(),
        services_section(),
        empresa_section(),
        obras_section(),
        tienda_section(),
        contacto_section(),
        footer(),
        background=NAVY,
        font_family=FONT_BODY,
        color=TEXT,
        width="100%",
        overflow_x="hidden",
    )
