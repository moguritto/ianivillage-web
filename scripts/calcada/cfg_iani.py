# Iani Village: copia calcada de la portada; textos legales de la copia anterior
DOMAIN = "ianivillage.com"
PAGES = {"": ""}
REDIRECTS = {"home/": "", "2026/": "", "thethirdwave/": "", "media/": "", "category/": ""}
EXTERNAL = {"aviso-legal/": None, "politica-de-privacidad/": None}
EXTERNAL = {}
INSTAGRAM = "https://www.instagram.com/"
EVENTON_STATIC = None
WA = "https://wa.me/34644632663"
BOTONES = ('<div class="elementor-widget-container" style="text-align:center;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">'
           f'<a class="elementor-button elementor-button-link elementor-size-sm" href="{WA}" target="_blank" rel="noopener">'
           '<span class="elementor-button-content-wrapper"><span class="elementor-button-text">Suscríbete por WhatsApp</span></span></a>'
           '<a class="elementor-button elementor-button-link elementor-size-sm" href="mailto:info@ianivillage.com?subject=Suscripci%C3%B3n">'
           '<span class="elementor-button-content-wrapper"><span class="elementor-button-text">Suscríbete por correo</span></span></a></div>')
WIDGETS = {
    "elementor-widget-form": BOTONES,
    "elementor-widget-ha-event-calendar": (
        '<div class="elementor-widget-container" style="text-align:center;padding:16px 0">'
        '<p>Consulta las próximas fechas de retiro por WhatsApp.</p>'
        f'<a class="elementor-button elementor-button-link elementor-size-sm" href="{WA}" target="_blank" rel="noopener">'
        '<span class="elementor-button-content-wrapper"><span class="elementor-button-text">Próximas fechas por WhatsApp</span></span></a></div>'),
}
SUBS = []
SUBS = [
    (r'<span class="elementor-icon-list-text">Aviso Legal</span>',
     '<a href="/aviso-legal/" style="color:inherit"><span class="elementor-icon-list-text">Aviso Legal</span></a>'),
    (r'<span class="elementor-icon-list-text">Política de Privacidad</span>',
     '<a href="/politica-de-privacidad/" style="color:inherit"><span class="elementor-icon-list-text">Política de Privacidad</span></a>'),
]
EXTRA_PAGES = ["aviso-legal/", "politica-de-privacidad/"]
