"""Páginas legales: Aviso Legal, Privacidad, Cookies y Calidad."""
import reflex as rx
from cofonta.styles import (
    NAVY, STEEL, SKY, WATER, WHITE, GOLD, MUTED, TEXT,
    FONT_HEADING, FONT_BODY, FONT_SERIF,
)
from cofonta.components import navbar, footer


GOOGLE_FONTS = "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap"


# ── Helpers compartidos ────────────────────────────────────────────────────────
def legal_shell(eyebrow_text: str, title: str, italic: str, updated: str, *sections) -> rx.Component:
    return rx.box(
        rx.el.link(rel="stylesheet", href=GOOGLE_FONTS),
        navbar(),
        # Hero
        rx.box(
            rx.hstack(
                rx.box(width="30px", height="1px", background=GOLD),
                rx.text(eyebrow_text, font_family=FONT_BODY, font_size="0.7rem",
                        letter_spacing="0.25em", text_transform="uppercase", color=GOLD),
                align="center", gap="1rem", margin_bottom="1rem",
            ),
            rx.heading(
                title,
                rx.text.span(italic, font_family=FONT_SERIF, font_style="italic", color=WATER)
                if italic else rx.fragment(),
                font_family=FONT_HEADING,
                font_size=["2rem", "3rem", "4rem"],
                letter_spacing="0.05em", color=WHITE, line_height="1",
                as_="h1",
            ),
            rx.text(updated, font_family=FONT_BODY, font_size="0.78rem",
                    color=MUTED, font_weight="300", margin_top="1rem"),
            padding=["9rem 1.5rem 3rem", "9rem 1.5rem 3rem", "10rem 3rem 4rem"],
            background=f"linear-gradient(160deg, {NAVY} 0%, #0d2040 100%)",
            border_bottom="1px solid rgba(59,130,196,0.1)",
            width="100%",
        ),
        # Contenido
        rx.box(
            *sections,
            max_width="860px",
            margin="0 auto",
            padding=["3rem 1.5rem", "3rem 1.5rem", "5rem 3rem"],
        ),
        footer(),
        background=NAVY, font_family=FONT_BODY, color=TEXT,
        width="100%", overflow_x="hidden",
    )


def legal_section(eyebrow: str, *children) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(width="20px", height="1px", background=GOLD),
            rx.text(eyebrow, font_family=FONT_BODY, font_size="0.68rem",
                    letter_spacing="0.25em", text_transform="uppercase", color=GOLD),
            align="center", gap="0.8rem", margin_bottom="1.5rem",
        ),
        *children,
        margin_bottom="3.5rem",
        padding_bottom="3.5rem",
        border_bottom="1px solid rgba(59,130,196,0.1)",
        width="100%",
    )


def legal_p(*children, **kwargs) -> rx.Component:
    return rx.text(
        *children,
        font_family=FONT_BODY, font_weight="300", color=MUTED,
        font_size="0.92rem", line_height="1.85", margin_bottom="1rem",
        **kwargs,
    )


def data_row(label: str, value: str) -> rx.Component:
    return rx.flex(
        rx.text(label, font_family=FONT_BODY, font_weight="500",
                color=MUTED, font_size="0.88rem", min_width="200px"),
        rx.text(value, font_family=FONT_BODY, font_weight="300",
                color=TEXT, font_size="0.88rem", line_height="1.6"),
        direction="row",
        gap="1rem",
        padding_y="0.8rem",
        border_bottom="1px solid rgba(59,130,196,0.08)",
        width="100%",
        flex_wrap="wrap",
    )


def info_box(*children) -> rx.Component:
    return rx.box(
        *children,
        padding="1.5rem",
        background="rgba(28,52,82,0.4)",
        border="1px solid rgba(59,130,196,0.2)",
        border_left=f"3px solid {GOLD}",
        margin_y="1.5rem",
    )


# ── Aviso Legal ────────────────────────────────────────────────────────────────
@rx.page(route="/aviso-legal", title="Aviso Legal — COFONTA®")
def aviso_legal() -> rx.Component:
    return legal_shell(
        "Información legal", "Aviso ", "Legal",
        "Última actualización: marzo de 2026 · En cumplimiento de la Ley 34/2002 (LSSI-CE)",

        legal_section("1. Datos identificativos del titular",
            data_row("Razón social", "COFONTA, S.L."),
            data_row("NIF", "B-38795860"),
            data_row("Domicilio social", "Calle Las Higueras, n.º 8, Local 4, Edif. Alicia II — 38350 Tacoronte (Tenerife)"),
            data_row("Registro Mercantil", "Hoja TF-34.744, Folio 85, Tomo 2.654, Sección General, Inscripción 1.ª"),
            data_row("Teléfono", "922 563 501"),
            data_row("Email", "cofonta-oficina@cofonta.com"),
            data_row("Sitio web", "www.cofonta.com"),
        ),

        legal_section("2. Objeto y ámbito de aplicación",
            legal_p("El presente Aviso Legal regula el acceso y uso del sitio web www.cofonta.com, "
                    "titularidad de COFONTA, S.L. El acceso al Sitio Web implica la aceptación plena "
                    "y sin reservas de todas las disposiciones incluidas en este Aviso Legal, así como "
                    "en la Política de Privacidad y la Política de Cookies."),
        ),

        legal_section("3. Propiedad intelectual e industrial",
            legal_p("Todos los contenidos del Sitio Web son propiedad intelectual de COFONTA, S.L. o "
                    "de terceros que han autorizado su uso, y están protegidos por la normativa española "
                    "e internacional sobre propiedad intelectual e industrial."),
            legal_p("Queda expresamente prohibida la reproducción, distribución o comunicación pública "
                    "de los contenidos sin autorización expresa y por escrito de COFONTA, S.L."),
        ),

        legal_section("4. Condiciones de uso",
            legal_p("El usuario puede visualizar, imprimir y almacenar los contenidos del Sitio Web "
                    "única y exclusivamente para uso personal y privado, no comercial."),
            legal_p("Queda prohibido utilizar el Sitio Web con fines ilícitos, causar daños a los "
                    "sistemas informáticos, introducir virus o utilizar los contenidos con fines "
                    "comerciales sin autorización."),
        ),

        legal_section("5. Responsabilidad",
            legal_p("COFONTA, S.L. no garantiza la disponibilidad ininterrumpida del Sitio Web y no "
                    "será responsable de los daños derivados del acceso o uso del Sitio Web, ni de "
                    "los contenidos de páginas web de terceros accesibles a través de enlaces."),
        ),

        legal_section("6. Legislación aplicable y jurisdicción",
            legal_p("Las partes se someten, con renuncia expresa a cualquier otro fuero, a los "
                    "Juzgados y Tribunales de Santa Cruz de Tenerife."),
            info_box(
                legal_p("Para resolución alternativa de litigios en línea: ",
                        rx.link("https://ec.europa.eu/consumers/odr",
                                href="https://ec.europa.eu/consumers/odr",
                                color=SKY, target="_blank")),
            ),
        ),
    )


# ── Política de Privacidad ─────────────────────────────────────────────────────
@rx.page(route="/politica-privacidad", title="Política de Privacidad — COFONTA®")
def politica_privacidad() -> rx.Component:
    derechos = [
        ("Acceso", "Obtener confirmación sobre si tratamos sus datos y acceder a ellos."),
        ("Rectificación", "Solicitar la corrección de datos inexactos o incompletos."),
        ("Supresión", "Solicitar la eliminación de sus datos cuando ya no sean necesarios."),
        ("Limitación", "Solicitar que suspendamos el tratamiento en determinadas circunstancias."),
        ("Portabilidad", "Recibir sus datos en formato estructurado para transmitirlos a otro responsable."),
        ("Oposición", "Oponerse al tratamiento basado en interés legítimo o con fines de marketing."),
    ]
    return legal_shell(
        "Protección de datos", "Política de ", "Privacidad",
        "Última actualización: marzo de 2026 · Conforme al RGPD (UE) 2016/679 y la LOPDGDD 3/2018",

        legal_section("1. Responsable del tratamiento",
            data_row("Responsable", "COFONTA, S.L."),
            data_row("NIF", "B-38795860"),
            data_row("Dirección", "Calle Las Higueras, n.º 8, Local 4, Edif. Alicia II — 38350 Tacoronte (Tenerife)"),
            data_row("Email", "cofonta-oficina@cofonta.com"),
        ),

        legal_section("2. Finalidades y bases jurídicas",
            legal_p("COFONTA, S.L. trata sus datos para: atender consultas y presupuestos "
                    "(base: medidas precontractuales), gestión de la relación contractual "
                    "(base: ejecución del contrato), cumplimiento de obligaciones legales "
                    "(base: obligación legal) y comunicaciones comerciales a clientes existentes "
                    "(base: interés legítimo / consentimiento)."),
        ),

        legal_section("3. Sus derechos",
            rx.grid(
                *[
                    rx.box(
                        rx.text(title, font_family=FONT_BODY, font_weight="500",
                                color=SKY, font_size="0.8rem", margin_bottom="0.4rem"),
                        rx.text(desc, font_family=FONT_BODY, font_weight="300",
                                color=MUTED, font_size="0.82rem"),
                        padding="1.2rem",
                        background="rgba(28,52,82,0.4)",
                        border="1px solid rgba(59,130,196,0.15)",
                    )
                    for title, desc in derechos
                ],
                columns=["1", "2", "2"],
                gap="1rem",
                margin_bottom="1.5rem",
            ),
            legal_p("Para ejercitar sus derechos, escríbanos a cofonta-oficina@cofonta.com "
                    "adjuntando copia de su DNI. Responderemos en el plazo máximo de un mes."),
            info_box(
                legal_p("Puede reclamar ante la Agencia Española de Protección de Datos (AEPD) en ",
                        rx.link("www.aepd.es", href="https://www.aepd.es",
                                color=SKY, target="_blank"), "."),
            ),
        ),

        legal_section("4. Seguridad y modificaciones",
            legal_p("COFONTA, S.L. ha adoptado las medidas técnicas y organizativas necesarias para "
                    "garantizar la seguridad de los datos personales y evitar su alteración, pérdida "
                    "o acceso no autorizado."),
            legal_p("Nos reservamos el derecho a modificar esta política para adaptarla a novedades "
                    "legislativas. Los cambios se anunciarán en el Sitio Web."),
        ),
    )


# ── Política de Cookies ────────────────────────────────────────────────────────
@rx.page(route="/politica-cookies", title="Política de Cookies — COFONTA®")
def politica_cookies() -> rx.Component:
    cookies = [
        ("cofonta_cookie_consent", "Necesaria", "Propia", "Guarda las preferencias de consentimiento.", "12 meses"),
        ("_ga",                    "Analítica",  "Google", "Distingue usuarios únicos para análisis de tráfico.", "2 años"),
        ("_ga_XXXXXXXXXX",         "Analítica",  "Google", "Mantiene el estado de sesión para estadísticas.", "2 años"),
        ("_gid",                   "Analítica",  "Google", "Distingue usuarios para estadísticas diarias.", "24 horas"),
    ]
    browsers = [
        ("Google Chrome",   "https://support.google.com/chrome/answer/95647"),
        ("Mozilla Firefox", "https://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies"),
        ("Apple Safari",    "https://support.apple.com/es-es/guide/safari/sfri11471"),
        ("Microsoft Edge",  "https://support.microsoft.com/es-es/microsoft-edge/eliminar-las-cookies-en-microsoft-edge-63947406"),
    ]
    return legal_shell(
        "Navegación y privacidad", "Política de ", "Cookies",
        "Última actualización: enero de 2025 · Conforme a la Directiva 2009/136/CE y Guía AEPD 2023",

        legal_section("1. ¿Qué son las cookies?",
            legal_p("Las cookies son pequeños archivos de texto que los sitios web almacenan en el "
                    "dispositivo del usuario. Su función es recordar las acciones y preferencias del "
                    "usuario durante un período de tiempo."),
        ),

        legal_section("2. Cookies utilizadas en este sitio web",
            legal_p("Este sitio web NO utiliza cookies de publicidad ni de marketing comportamental. "
                    "Las cookies analíticas solo se activan con consentimiento del usuario."),
            rx.box(
                # Cabecera tabla
                rx.grid(
                    *[rx.text(h, font_family=FONT_BODY, font_size="0.68rem",
                              letter_spacing="0.15em", text_transform="uppercase",
                              color=GOLD, padding="0.7rem 1rem",
                              border_bottom=f"1px solid rgba(201,168,76,0.3)")
                      for h in ["Cookie", "Tipo", "Titular", "Finalidad", "Duración"]],
                    columns="5", width="100%",
                ),
                # Filas
                *[
                    rx.grid(
                        *[rx.text(cell, font_family=FONT_BODY, font_size="0.85rem",
                                  font_weight="300", color=MUTED, padding="0.85rem 1rem",
                                  border_bottom="1px solid rgba(59,130,196,0.08)",
                                  line_height="1.6")
                          for cell in row],
                        columns="5", width="100%",
                    )
                    for row in cookies
                ],
                overflow_x="auto",
                width="100%",
            ),
        ),

        legal_section("3. Cómo deshabilitar cookies desde el navegador",
            *[
                rx.hstack(
                    rx.text(name, font_family=FONT_BODY, font_weight="400",
                            color=TEXT, font_size="0.88rem", min_width="180px"),
                    rx.link(url, href=url, color=SKY, font_family=FONT_BODY,
                            font_size="0.85rem", font_weight="300",
                            text_decoration="none", _hover={"color": WATER},
                            target="_blank"),
                    gap="1rem", padding_y="0.8rem",
                    border_bottom="1px solid rgba(59,130,196,0.08)",
                    width="100%", flex_wrap="wrap",
                )
                for name, url in browsers
            ],
        ),

        legal_section("4. Transferencias internacionales",
            legal_p("Google LLC está acogida al Marco de Privacidad de Datos UE-EE.UU. (Data Privacy "
                    "Framework), aprobado por la Comisión Europea en julio de 2023."),
        ),
    )


# ── Política de Calidad ────────────────────────────────────────────────────────
@rx.page(route="/politica-calidad", title="Política de Calidad — COFONTA®")
def politica_calidad() -> rx.Component:
    principios = [
        ("01", "Enfoque al cliente",
         "La satisfacción del cliente es el fin último de nuestra organización."),
        ("02", "Mejora continua",
         "La mejora de nuestros procesos es un objetivo prioritario y permanente."),
        ("03", "Trabajo en equipo",
         "La calidad es responsabilidad de toda la organización."),
        ("04", "Materiales de primera calidad",
         "Usamos exclusivamente materiales homologados y con certificación."),
        ("05", "Nuevas tecnologías",
         "Apostamos por la incorporación de tecnología para la mejora de nuestra gestión."),
    ]
    objetivos = [
        "Cumplir la normativa técnica aplicable a cada tipo de instalación.",
        "Alcanzar el máximo nivel de satisfacción de nuestros clientes.",
        "Cumplir los plazos de ejecución comprometidos con el cliente.",
        "Reducir al mínimo el número de no conformidades e incidencias.",
        "Mantener a todo el personal técnico permanentemente formado.",
        "Seleccionar y evaluar periódicamente a proveedores y subcontratistas.",
        "Avanzar hacia la implantación de un Sistema de Gestión conforme a ISO 9001.",
    ]
    return legal_shell(
        "Compromiso con la excelencia", "Política de ", "Calidad",
        "Revisión: marzo de 2026 · COFONTA, S.L. — NIF B-38795860",

        legal_section("Declaración de política de calidad",
            legal_p("COFONTA, S.L. considera que el compromiso con la calidad es un requisito "
                    "fundamental para la continuidad y el crecimiento de la empresa. Nuestro objetivo "
                    "final es la Calidad Total en todas y cada una de las obras e instalaciones."),
        ),

        legal_section("Principios fundamentales",
            rx.grid(
                *[
                    rx.box(
                        rx.text(num, font_family=FONT_HEADING, font_size="4rem",
                                color="rgba(59,130,196,0.08)", line_height="1",
                                position="absolute", top="-0.5rem", right="1rem"),
                        rx.text(title, font_family=FONT_BODY, font_weight="500",
                                color=SKY, font_size="0.88rem", margin_bottom="0.6rem"),
                        rx.text(desc, font_family=FONT_BODY, font_weight="300",
                                color=MUTED, font_size="0.85rem", line_height="1.7"),
                        padding="2rem",
                        background="rgba(28,52,82,0.4)",
                        border="1px solid rgba(59,130,196,0.15)",
                        position="relative",
                        overflow="hidden",
                    )
                    for num, title, desc in principios
                ],
                columns=["1", "2", "2"],
                gap="1.5rem",
            ),
        ),

        legal_section("Objetivos de calidad",
            rx.vstack(
                *[
                    rx.hstack(
                        rx.text("✓", color=SKY, font_size="0.9rem", min_width="20px"),
                        rx.text(obj, font_family=FONT_BODY, font_weight="300",
                                color=MUTED, font_size="0.9rem", line_height="1.6"),
                        align="flex-start", gap="1rem",
                        padding_y="1.1rem",
                        border_bottom="1px solid rgba(59,130,196,0.1)",
                        width="100%",
                    )
                    for obj in objetivos
                ],
                gap="0", width="100%",
            ),
        ),

        legal_section("Política de seguridad y salud",
            legal_p("COFONTA, S.L. dispone de una Evaluación Inicial de Riesgos Laborales y elabora "
                    "un estudio de riesgos específico para cada obra. Cuenta con póliza de "
                    "Responsabilidad Civil vigente y todos los seguros obligatorios de convenio."),
            rx.grid(
                *[
                    rx.vstack(
                        rx.text(icon, font_size="1.8rem"),
                        rx.text(title, font_family=FONT_BODY, font_weight="500",
                                color=WHITE, font_size="0.82rem", margin_top="0.5rem"),
                        rx.text(desc, font_family=FONT_BODY, font_weight="300",
                                color=MUTED, font_size="0.8rem", line_height="1.5",
                                text_align="center"),
                        align="center", padding="1.5rem",
                        background="rgba(28,52,82,0.4)",
                        border="1px solid rgba(59,130,196,0.12)",
                        gap="0.2rem",
                    )
                    for icon, title, desc in [
                        ("🛡️", "Siniestralidad cero", "Objetivo de índice del 0% mediante formación y EPIs adecuados."),
                        ("👥", "Formación continua",   "Formación periódica en prevención, seguridad y salud laboral."),
                        ("📋", "Seguros y cobertura",  "Póliza de RC vigente y todos los seguros obligatorios de convenio."),
                    ]
                ],
                columns="3", gap="1rem", margin_top="1.5rem",
            ),
        ),

        legal_section("Aprobación y vigencia",
            rx.box(
                rx.text("Aprobado por la Dirección",
                        font_family=FONT_BODY, font_size="0.7rem",
                        letter_spacing="0.2em", text_transform="uppercase",
                        color=GOLD, margin_bottom="1rem"),
                rx.text("COFONTA, S.L.",
                        font_family=FONT_HEADING, font_size="1.8rem",
                        letter_spacing="0.08em", color=WHITE),
                rx.text("Gerencia", font_family=FONT_BODY, font_weight="300",
                        color=MUTED, font_size="0.82rem", margin_top="0.3rem"),
                rx.text("Tacoronte (Tenerife), marzo de 2026",
                        font_family=FONT_BODY, font_weight="300",
                        color=MUTED, font_size="0.8rem", margin_top="0.8rem"),
                padding="2rem",
                border="1px solid rgba(59,130,196,0.2)",
                background="rgba(28,52,82,0.3)",
            ),
        ),
    )
