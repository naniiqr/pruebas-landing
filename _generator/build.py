# -*- coding: utf-8 -*-
"""
Generates the static D'Ara Perruqueria site (Catalan) into /home/claude/dara/site
Flat file structure so it works directly on GitHub Pages at /<repo>/ root.
"""
import os

ROOT = "/home/claude/dara/site"

# ---------------------------------------------------------------------------
# Shared data
# ---------------------------------------------------------------------------

PHONE_DISPLAY = "972 67 28 27"
PHONE_TEL = "+34972672827"
WHATSAPP_NUMBER = "34972672827"
ADDRESS = "Carrer Méndez Núñez, 41, 17600 Figueres, Girona"
MAP_EMBED = ("https://www.google.com/maps?q=" +
             "Carrer+Mendez+Nunez+41+17600+Figueres+Girona&output=embed")

SERVICES = [
    {
        "slug": "talls-i-canvi-destil",
        "nav": "Talls i canvi d'estil",
        "title": "Talls i canvi d'estil",
        "card_line": "Un nou tall, una nova manera de veure't.",
        "hero_img": "cut-smile.jpg",
        "detail_img": "cut-detail.jpg",
        "num": "01",
        "subhead": "Un nou tall, una nova manera de veure't",
        "paras": [
            "A Perruqueria D'Ara t'ajudem a trobar el tall i l'estil que millor encaixen amb tu, la teva personalitat i el teu dia a dia. Analitzem els teus trets, el tipus de cabell i les teves preferències per crear un resultat natural, actual i fàcil de mantenir.",
            "Tant si busques un petit canvi de look com si vols una transformació completa, posem la nostra experiència i creativitat al teu servei.",
        ],
        "features": [
            "Talls personalitzats",
            "Assessorament d'estil",
            "Canvis de look",
            "Adaptació del tall al tipus de cabell",
            "Talls actuals i tendències",
            "Acabats i pentinats",
        ],
        "note": "Deixa't assessorar i descobreix un estil que parli de tu. A D'Ara convertim cada tall en una oportunitat per renovar-te.",
    },
    {
        "slug": "pentinats",
        "nav": "Pentinats",
        "title": "Pentinats",
        "card_line": "Un pentinat que s'adapta al teu estil i a cada ocasió.",
        "hero_img": "updo-braid.jpg",
        "detail_img": "shelf-products.jpg",
        "num": "02",
        "subhead": "Troba el pentinat que millor encaixa amb tu",
        "paras": [
            "A Perruqueria D'Ara creem pentinats personalitzats per a cada estil i ocasió. Treballem el cabell amb cura i precisió per aconseguir un acabat natural, elegant i durador.",
            "Des d'un look senzill i desenfadat fins a un pentinat més sofisticat per a una ocasió especial, t'assessorem per trobar la proposta que millor s'adapta al teu cabell, al teu estil i a la teva personalitat.",
        ],
        "features": [
            "Ones i trenes",
            "Recollits i semi-recollits",
            "Pentinats per a esdeveniments",
            "Cabells solts amb moviment",
            "Assessorament personalitzat",
            "Acabats de llarga durada",
        ],
        "note": "Un bon pentinat no només transforma el teu cabell, també potencia el teu estil.",
    },
    {
        "slug": "tractaments-de-recuperacio-capillar",
        "nav": "Tractaments de recuperació capil·lar",
        "title": "Tractaments de recuperació capil·lar",
        "card_line": "Recupera la força, la vitalitat i la bellesa natural del teu cabell.",
        "hero_img": "curly-treatment.jpg",
        "detail_img": "curly-detail.jpg",
        "num": "03",
        "subhead": "Recupera la força, la vitalitat i la bellesa natural del teu cabell",
        "paras": [
            "A Perruqueria D'Ara oferim tractaments de recuperació capil·lar pensats per cuidar en profunditat els cabells debilitats, secs, danyats o sensibilitzats.",
            "Analitzem les necessitats del teu cabell i seleccionem el tractament més adequat per ajudar a reparar, hidratar i reforçar la fibra capil·lar, millorant-ne la textura, la brillantor i l'aspecte.",
        ],
        "features": [
            "Diagnòstic capil·lar previ",
            "Hidratació profunda",
            "Reparació de la fibra capil·lar",
            "Reducció de l'encrespament",
            "Recuperació post-color",
            "Rutines de manteniment a casa",
        ],
        "note": "Cuida el teu cabell avui per tornar a lluir-lo com mai.",
    },
    {
        "slug": "tecniques-de-color-tints-i-metxes",
        "nav": "Tècniques de color, tints i metxes",
        "title": "Tècniques de color, tints i metxes",
        "card_line": "Dona color al teu estil i troba el to que millor parla de tu.",
        "hero_img": "color-foil.jpg",
        "detail_img": "color-smile.jpg",
        "num": "04",
        "subhead": "Dona color al teu estil i troba el to que millor parla de tu",
        "paras": [
            "A Perruqueria D'Ara treballem diferents tècniques de coloració per aconseguir resultats personalitzats, naturals i actuals. T'assessorem per trobar el color, el matís i la tècnica que millor s'adapten al teu estil, al teu tipus de cabell i al resultat que vols aconseguir.",
            "Des d'un canvi de color complet fins a unes metxes subtils que aportin llum i dimensió, cuidem cada detall perquè el resultat sigui harmònic i afavoreixi els teus trets.",
        ],
        "features": [
            "Tints i coloració personalitzada",
            "Metxes i reflexos",
            "Tècniques d'il·luminació",
            "Canvis de color",
            "Correcció i renovació del color",
            "Assessorament personalitzat",
        ],
        "note": "Un bon color transforma el teu look. Nosaltres t'ajudem a trobar el teu.",
    },
    {
        "slug": "allisats-organics",
        "nav": "Allisats orgànics",
        "title": "Allisats orgànics",
        "card_line": "Un cabell més llis, suau i manejable, sense renunciar a la seva naturalitat.",
        "hero_img": "blonde-glow.jpg",
        "detail_img": "curly-detail.jpg",
        "num": "05",
        "subhead": "Un cabell més llis, suau i manejable, sense renunciar a la seva naturalitat",
        "paras": [
            "A Perruqueria D'Ara oferim allisats orgànics pensats per reduir l'encrespament, controlar el volum i facilitar el pentinat, respectant al màxim la fibra capil·lar.",
            "T'assessorem segons el teu tipus de cabell i les seves necessitats per aconseguir un resultat suau, brillant i fàcil de mantenir, sense perdre el moviment i l'aspecte natural del cabell.",
        ],
        "features": [
            "Reducció de l'encrespament",
            "Control del volum",
            "Respecte per la fibra capil·lar",
            "Acabat natural i brillant",
            "Ideal per a cabells rebels o amb frizz",
            "Fàcil manteniment diari",
        ],
        "note": "Descobreix un cabell més suau, disciplinat i fàcil de pentinar.",
    },
    {
        "slug": "pentinats-de-nuvia",
        "nav": "Pentinats de núvia",
        "title": "Pentinats de núvia",
        "card_line": "El pentinat perfecte per a un dia que recordaràs sempre.",
        "hero_img": "bridal-braid.jpg",
        "detail_img": "wall-logo-orchid.jpg",
        "num": "06",
        "subhead": "El pentinat perfecte per a un dia que recordaràs sempre",
        "paras": [
            "A Perruqueria D'Ara creem pentinats de núvia personalitzats, cuidant cada detall perquè et sentis còmoda, elegant i fidel al teu estil.",
            "T'assessorem tenint en compte el vestit, els complements, el tipus de cabell i la forma del rostre per trobar el pentinat que millor encaixi amb tu i amb l'estil del teu casament.",
        ],
        "features": [
            "Prova de pentinat prèvia",
            "Recollits elegants",
            "Trenes i semi-recollits",
            "Ones suaus i cabells solts",
            "Complements i flors naturals",
            "Servei coordinat amb maquillatge",
        ],
        "note": "Deixa'ns formar part del teu gran dia i fem que el teu pentinat sigui tan especial com tu.",
    },
]

REVIEWS = [
    {
        "initials": "MR",
        "name": "Marta R.",
        "meta": "Clienta des de fa 3 anys",
        "quote": "Cada vegada que hi vaig, surto sentint-me jo mateixa però millor. Escolten el que vols i no et venen un canvi que no has demanat.",
    },
    {
        "initials": "LP",
        "name": "Laia P.",
        "meta": "Tractament capil·lar",
        "quote": "Vaig arribar amb el cabell molt malmès per les decoloracions i em van proposar un pla de recuperació real, pas a pas. Es nota moltíssim.",
    },
    {
        "initials": "SC",
        "name": "Sílvia C.",
        "meta": "Pentinat de núvia",
        "quote": "Vam fer una prova abans del casament i el dia B tot va anar perfecte. Puntuals, atentes i el pentinat va aguantar tota la nit.",
    },
]

GALLERY = [
    ("reception-desk.jpg", "wide"),
    ("wash-chairs.jpg", ""),
    ("shelf-products.jpg", "tall"),
    ("entrance-door.jpg", ""),
    ("storefront.jpg", ""),
    ("wall-logo-orchid.jpg", ""),
    ("salon-wide.jpg", "wide"),
    ("cut-detail.jpg", ""),
]

NAV_PAGES = [
    ("index.html", "Inici"),
]

FOOTER_LEGAL = [
    ("privacitat.html", "Política de privacitat"),
    ("avis-legal.html", "Avís legal"),
    ("cookies.html", "Polítiques de cookies"),
]

# ---------------------------------------------------------------------------
# Icons (inline SVG, currentColor)
# ---------------------------------------------------------------------------

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z" opacity="0"></path><path d="M22 6 12 13 2 6"></path><rect x="2" y="4" width="20" height="16" rx="2"></rect></svg>'
ICON_CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
ICON_WA = '<svg viewBox="0 0 32 32"><path d="M16.04 3C9.09 3 3.46 8.63 3.46 15.58c0 2.5.68 4.85 1.98 6.9L3 29l6.7-2.4a12.5 12.5 0 0 0 6.34 1.72h.01c6.95 0 12.58-5.63 12.58-12.58C28.63 8.79 23 3 16.04 3zm0 22.9h-.01a10.3 10.3 0 0 1-5.25-1.44l-.38-.22-3.98 1.43 1.34-3.88-.24-.4a10.28 10.28 0 0 1-1.58-5.47c0-5.69 4.63-10.32 10.11-10.32 2.7 0 5.24 1.05 7.15 2.96a10.05 10.05 0 0 1 2.96 7.16c0 5.69-4.63 10.18-10.12 10.18zm5.55-7.63c-.3-.15-1.79-.88-2.07-.98-.28-.1-.48-.15-.68.15-.2.3-.78.98-.96 1.18-.18.2-.35.22-.65.07-.3-.15-1.27-.47-2.42-1.5-.9-.8-1.5-1.79-1.68-2.09-.18-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.68-1.65-.94-2.26-.25-.6-.5-.5-.68-.51h-.58c-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47s1.06 2.86 1.21 3.06c.15.2 2.09 3.2 5.08 4.48.71.31 1.26.49 1.69.62.71.23 1.36.2 1.87.12.57-.09 1.79-.73 2.04-1.44.25-.71.25-1.31.18-1.44-.07-.13-.27-.2-.57-.35z"></path></svg>'

def checker_favicon():
    return ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E"
            "%3Crect width='20' height='20' fill='%23211d1b'/%3E"
            "%3Crect x='20' y='20' width='20' height='20' fill='%23211d1b'/%3E"
            "%3Crect x='20' width='20' height='20' fill='%23f6f0e8'/%3E"
            "%3Crect y='20' width='20' height='20' fill='%23f6f0e8'/%3E%3C/svg%3E")

# ---------------------------------------------------------------------------
# Shared chrome
# ---------------------------------------------------------------------------

def nav_html(active=""):
    dropdown_items = "".join(
        '<li><a href="{slug}.html">{nav}</a></li>'.format(slug=s["slug"], nav=s["nav"])
        for s in SERVICES
    )
    return """
  <header class="site-header">
    <nav class="nav">
      <a href="index.html" class="logo">
        <span class="mark">D'Ara</span>
        <span class="sub">Perruqueria</span>
      </a>

      <ul class="nav-links" id="nav-links">
        <li><a class="top-link" href="index.html"{inici_current}>Inici</a></li>
        <li class="has-dropdown">
          <a class="top-link" href="{first_service}.html"{serveis_current}>Serveis <span class="caret"></span></a>
          <ul class="dropdown">
            {dropdown_items}
          </ul>
        </li>
        <li><a class="top-link" href="situacio-i-contacte.html"{contacte_current}>Situació i contacte</a></li>
      </ul>

      <div class="nav-cta">
        <a class="phone-pill" href="tel:{phone_tel}">{icon_phone}<span>{phone_display}</span></a>
        <button class="nav-toggle" aria-label="Obre el menú" aria-expanded="false" aria-controls="nav-links">
          <span></span>
        </button>
      </div>
    </nav>
  </header>
""".format(
        inici_current=' aria-current="page"' if active == "inici" else "",
        serveis_current=' aria-current="page"' if active == "serveis" else "",
        contacte_current=' aria-current="page"' if active == "contacte" else "",
        first_service=SERVICES[0]["slug"],
        dropdown_items=dropdown_items,
        phone_tel=PHONE_TEL,
        phone_display=PHONE_DISPLAY,
        icon_phone=ICON_PHONE,
    )


def footer_html():
    services_links = "".join(
        '<li><a href="{slug}.html">{nav}</a></li>'.format(slug=s["slug"], nav=s["nav"])
        for s in SERVICES
    )
    legal_links_footer_col = "".join(
        '<li><a href="{f}">{t}</a></li>'.format(f=f, t=t) for f, t in FOOTER_LEGAL
    )
    legal_links_bottom = "".join(
        '<a href="{f}">{t}</a>'.format(f=f, t=t) for f, t in FOOTER_LEGAL
    )
    year = "2026"
    return """
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <a href="index.html" class="logo">
            <span class="mark">D'Ara</span>
            <span class="sub">Perruqueria</span>
          </a>
          <p class="footer-about">Perruqueria a Figueres amb més de 35 anys d'experiència cuidant la imatge i el benestar dels nostres clients.</p>
        </div>
        <div class="footer-col">
          <h4>Serveis</h4>
          <ul>{services_links}</ul>
        </div>
        <div class="footer-col">
          <h4>Perruqueria</h4>
          <ul>
            <li><a href="index.html">Inici</a></li>
            <li><a href="situacio-i-contacte.html">Situació i contacte</a></li>
            <li><a href="tel:{phone_tel}">{phone_display}</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Visita'ns</h4>
          <ul>
            <li>{address}</li>
            <li><a href="https://wa.me/{wa}" target="_blank" rel="noopener">Escriu-nos per WhatsApp</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; {year} Perruqueria D'Ara. Tots els drets reservats.</span>
        <div class="legal-links">{legal_links_bottom}</div>
      </div>
    </div>
  </footer>

  <a class="wa-float" href="https://wa.me/{wa}" target="_blank" rel="noopener" aria-label="Escriu-nos per WhatsApp">
    {icon_wa}
  </a>

  <script src="js/main.js"></script>
""".format(
        services_links=services_links,
        legal_links_bottom=legal_links_bottom,
        phone_tel=PHONE_TEL,
        phone_display=PHONE_DISPLAY,
        address=ADDRESS,
        wa=WHATSAPP_NUMBER,
        year=year,
        icon_wa=ICON_WA,
    )


def page_shell(title, description, body, active="", extra_head=""):
    return """<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{favicon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="css/style.css">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Vés al contingut</a>
{nav}
<main id="main">
{body}
</main>
{footer}
</body>
</html>
""".format(
        title=title,
        description=description,
        favicon=checker_favicon(),
        extra_head=extra_head,
        nav=nav_html(active),
        body=body,
        footer=footer_html(),
    )


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", full)


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def build_index():
    svc_cards = ""
    for s in SERVICES:
        svc_cards += """
        <article class="svc-card">
          <a href="{slug}.html" class="thumb"><img src="images/{img}" alt="{title} — Perruqueria D'Ara Figueres" loading="lazy" width="600" height="470"></a>
          <div class="body">
            <span class="num">{num}</span>
            <h3><a href="{slug}.html">{title}</a></h3>
            <p>{line}</p>
            <a class="go" href="{slug}.html">Descobreix el servei {arrow}</a>
          </div>
        </article>""".format(
            slug=s["slug"], img=s["hero_img"], title=s["title"],
            num=s["num"], line=s["card_line"], arrow=ICON_ARROW,
        )

    gallery_items = ""
    for img, cls in GALLERY:
        gallery_items += '\n        <a href="images/{img}" class="{cls}"><img src="images/{img}" alt="Espai de Perruqueria D\'Ara a Figueres" loading="lazy"></a>'.format(img=img, cls=cls)

    review_cards = ""
    for r in REVIEWS:
        review_cards += """
        <div class="review-card">
          <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p>&ldquo;{quote}&rdquo;</p>
          <div class="who">
            <div class="avatar">{initials}</div>
            <div>
              <strong>{name}</strong>
              <span>{meta}</span>
            </div>
          </div>
        </div>""".format(quote=r["quote"], initials=r["initials"], name=r["name"], meta=r["meta"])

    body = """
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <span class="eyebrow">Perruqueria a Figueres · des de 1990</span>
        <h1>Tot el que és bo de la vida despentina.</h1>
        <p class="lede">Gaudeix del moment que per pentinar-te ja estem nosaltres. A Perruqueria D'Ara som una de les perruqueries de referència a Figueres — t'esperem al carrer Méndez Núñez.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="https://wa.me/{wa}" target="_blank" rel="noopener">{icon_wa_small} Reserva per WhatsApp</a>
          <a class="btn btn--ghost" href="tel:{phone_tel}">{icon_phone} Truca'ns</a>
        </div>
      </div>
      <div class="hero-media">
        <div class="frame"><img src="images/cut-smile.jpg" alt="Clienta somrient durant un tall de cabell a Perruqueria D'Ara" width="700" height="826"></div>
        <div class="tag">
          <span class="checker checker--pale" aria-hidden="true"></span>
          <span><strong>+35 anys</strong><span>cuidant la imatge de Figueres</span></span>
        </div>
      </div>
    </div>
  </section>

  <section class="about">
    <div class="wrap about-grid">
      <h2 class="reveal">La teva imatge és la nostra passió.</h2>
      <div class="about-copy reveal" style="--reveal-delay:.12s">
        <p>A <strong>Perruqueria D'Ara</strong>, amb més de 35 anys d'experiència, cuidem la imatge i el benestar dels nostres clients a Figueres. Creiem que cada persona és única i, per això, oferim un assessorament personalitzat per trobar l'estil que millor s'adapti a la teva personalitat i realci la teva bellesa natural.</p>
        <p>Un equip de professionals que treballa amb passió, experiència i les últimes tendències en perruqueria, utilitzant productes de primera qualitat per garantir uns resultats excel·lents i un cabell sa, brillant i cuidat.</p>
        <p>Tant si busques un canvi d'imatge, un tall, un color, unes metxes o un tractament capil·lar, a D'Ara trobaràs un espai modern, acollidor i pensat perquè gaudeixis d'una experiència única.</p>
      </div>
    </div>
  </section>

  <section class="services" id="serveis">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Els nostres serveis</span>
        <h2>Vine a descobrir tot el que podem fer per tu.</h2>
        <p>Sis maneres de cuidar el teu cabell, totes amb el mateix mim i el mateix assessorament personalitzat.</p>
      </div>
      <div class="svc-grid stagger">{svc_cards}
      </div>
    </div>
  </section>

  <section class="gallery">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">L'espai D'Ara</span>
        <h2>Un racó modern i acollidor al centre de Figueres.</h2>
        <p>Terra de quadres, llum natural i un equip que et rebrà com a casa.</p>
      </div>
      <div class="gallery-grid stagger">{gallery_items}
      </div>
    </div>
  </section>

  <section class="reviews">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">El que opinen els nostres clients</span>
        <h2>Persones que ja s'han deixat assessorar.</h2>
      </div>
      <div class="reviews-badge reveal">
        <span class="score">4.8</span>
        <div class="meta">
          <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
          <small>Valoracions de clientes de Perruqueria D'Ara</small>
        </div>
      </div>
      <div class="reviews-grid stagger">{review_cards}
      </div>
    </div>
  </section>

  <section class="cta-banner">
    <div class="wrap reveal">
      <h2>La teva imatge es mereix una cita.</h2>
      <div class="btn-row">
        <a class="btn btn--primary" href="https://wa.me/{wa}" target="_blank" rel="noopener">{icon_wa_small} Reserva per WhatsApp</a>
        <a class="btn btn--on-dark" href="situacio-i-contacte.html">Com arribar</a>
      </div>
    </div>
  </section>
""".format(
        svc_cards=svc_cards,
        gallery_items=gallery_items,
        review_cards=review_cards,
        wa=WHATSAPP_NUMBER,
        phone_tel=PHONE_TEL,
        icon_wa_small='<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.87.51 3.63 1.4 5.14L2 22l5.13-1.48a9.85 9.85 0 0 0 4.91 1.31h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.13-2.9-7C17.18 3.03 14.7 2 12.04 2z" opacity="0"></path><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.13.3-.35.44-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.03 1-1.03 2.44s1.05 2.83 1.2 3.03c.15.2 2.06 3.15 5 4.42.7.3 1.24.48 1.67.62.7.22 1.34.19 1.84.12.56-.08 1.76-.72 2.01-1.42.25-.7.25-1.3.17-1.42-.07-.13-.27-.2-.57-.35z"></path><path d="M12.04 21.35a9.4 9.4 0 0 1-4.79-1.31l-.34-.2-3.56 1.03 1.06-3.5-.22-.36a9.4 9.4 0 0 1-1.45-5.1c0-5.2 4.23-9.44 9.4-9.44a9.35 9.35 0 0 1 6.65 2.76 9.31 9.31 0 0 1 2.75 6.65c0 5.2-4.23 9.47-9.4 9.47zm0-20.35C6.5 1 2 5.5 2 11.03c0 1.9.5 3.7 1.44 5.28L2 22l5.83-1.53a10.85 10.85 0 0 0 5.21 1.33h.01C18.5 21.8 23 17.3 23 11.77 23 6.24 18.5 1 12.04 1z"></path></svg>',
        icon_phone=ICON_PHONE,
    )

    write("index.html", page_shell(
        title="Perruqueria D'Ara — Perruqueria a Figueres",
        description="Perruqueria D'Ara, a Figueres: talls, pentinats, color, tractaments capil·lars, allisats orgànics i pentinats de núvia. Més de 35 anys d'experiència.",
        body=body,
        active="inici",
    ))


# ---------------------------------------------------------------------------
# Service detail pages
# ---------------------------------------------------------------------------

def build_service_pages():
    for i, s in enumerate(SERVICES):
        paras_html = "\n          ".join("<p>{}</p>".format(p) for p in s["paras"])
        features_html = "\n            ".join("<li>{}</li>".format(f) for f in s["features"])

        chips = ""
        for other in SERVICES:
            current = ' aria-current="page"' if other["slug"] == s["slug"] else ""
            chips += '<a class="chip" href="{slug}.html"{cur}>{nav}</a>\n            '.format(
                slug=other["slug"], cur=current, nav=other["nav"])

        body = """
  <section class="page-hero">
    <img src="images/{hero_img}" alt="{title} a Perruqueria D'Ara Figueres" width="1600" height="900">
    <div class="wrap">
      <div class="breadcrumb">
        <a href="index.html">Inici</a><span>/</span><a href="index.html#serveis">Serveis</a><span>/</span><span>{title}</span>
      </div>
      <h1>{title}</h1>
    </div>
  </section>

  <section class="detail">
    <div class="wrap detail-grid">
      <div class="frame reveal-scale"><img src="images/{detail_img}" alt="Detall del servei {title} a Perruqueria D'Ara" loading="lazy" width="700" height="756"></div>
      <div class="detail-copy reveal" style="--reveal-delay:.1s">
        <span class="eyebrow">Servei {num}</span>
        <h2>{subhead}</h2>
        {paras_html}
        <ul class="feature-list">
            {features_html}
        </ul>
        <p class="detail-note">{note}</p>
        <div class="btn-row" style="margin-top:32px;">
          <a class="btn btn--primary" href="https://wa.me/{wa}" target="_blank" rel="noopener">Reserva per WhatsApp</a>
          <a class="btn btn--ghost" href="tel:{phone_tel}">Truca'ns · {phone_display}</a>
        </div>
      </div>
    </div>
  </section>

  <section class="other-services">
    <div class="wrap">
      <div class="section-head reveal" style="margin-bottom:32px;">
        <span class="eyebrow">Descobreix més</span>
        <h2>La resta dels nostres serveis</h2>
      </div>
      <div class="chip-row">
        {chips}
      </div>
    </div>
  </section>
""".format(
            hero_img=s["hero_img"], title=s["title"], detail_img=s["detail_img"],
            num=s["num"], subhead=s["subhead"], paras_html=paras_html,
            features_html=features_html, note=s["note"], chips=chips,
            wa=WHATSAPP_NUMBER, phone_tel=PHONE_TEL, phone_display=PHONE_DISPLAY,
        )

        write(s["slug"] + ".html", page_shell(
            title="{} — Perruqueria D'Ara Figueres".format(s["title"]),
            description="{} a Perruqueria D'Ara, Figueres. {}".format(s["title"], s["card_line"]),
            body=body,
            active="serveis",
        ))


# ---------------------------------------------------------------------------
# Contact page
# ---------------------------------------------------------------------------

def build_contact():
    body = """
  <section class="page-hero">
    <img src="images/reception-desk.jpg" alt="Recepció de Perruqueria D'Ara a Figueres" width="1600" height="900">
    <div class="wrap">
      <div class="breadcrumb">
        <a href="index.html">Inici</a><span>/</span><span>Situació i contacte</span>
      </div>
      <h1>Situació i contacte</h1>
    </div>
  </section>

  <section class="contact">
    <div class="wrap contact-grid">
      <div class="contact-card reveal">
        <div class="contact-item">
          <span class="ico">{icon_pin}</span>
          <div>
            <strong>Adreça</strong>
            <p>{address}</p>
          </div>
        </div>
        <div class="contact-item">
          <span class="ico">{icon_phone}</span>
          <div>
            <strong>Telèfon</strong>
            <a href="tel:{phone_tel}">{phone_display}</a>
          </div>
        </div>
        <div class="contact-item">
          <span class="ico">{icon_wa}</span>
          <div>
            <strong>WhatsApp</strong>
            <a href="https://wa.me/{wa}" target="_blank" rel="noopener">Escriu-nos per reservar cita</a>
          </div>
        </div>
        <div class="contact-item">
          <span class="ico">{icon_clock}</span>
          <div>
            <strong>Hores</strong>
            <p>Amb cita prèvia. Truca'ns o escriu-nos per WhatsApp i et confirmarem el millor horari.</p>
          </div>
        </div>
        <div class="btn-row" style="margin-top:30px;">
          <a class="btn btn--primary" href="https://wa.me/{wa}" target="_blank" rel="noopener">Reserva per WhatsApp</a>
        </div>
      </div>
      <div class="map-frame reveal" style="--reveal-delay:.12s">
        <iframe src="{map_embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de Perruqueria D'Ara a Figueres"></iframe>
      </div>
    </div>
  </section>

  <section class="cta-banner">
    <div class="wrap reveal">
      <h2>T'esperem a la nostra perruqueria de Figueres.</h2>
      <div class="btn-row">
        <a class="btn btn--primary" href="tel:{phone_tel}">Truca'ns ara</a>
      </div>
    </div>
  </section>
""".format(
        icon_pin=ICON_PIN, icon_phone=ICON_PHONE, icon_wa=ICON_WA, icon_clock=ICON_CLOCK,
        address=ADDRESS, phone_tel=PHONE_TEL, phone_display=PHONE_DISPLAY,
        wa=WHATSAPP_NUMBER, map_embed=MAP_EMBED,
    )

    write("situacio-i-contacte.html", page_shell(
        title="Situació i contacte — Perruqueria D'Ara Figueres",
        description="Troba Perruqueria D'Ara a {}. Truca'ns al {} o escriu-nos per WhatsApp.".format(ADDRESS, PHONE_DISPLAY),
        body=body,
        active="contacte",
    ))


# ---------------------------------------------------------------------------
# Legal placeholder pages
# ---------------------------------------------------------------------------

def build_legal():
    pages = {
        "privacitat.html": (
            "Política de privacitat",
            """
            <p>Aquesta pàgina descriu, a mode de resum, com Perruqueria D'Ara tracta les dades personals de les persones que es posen en contacte a través d'aquest lloc web (per exemple, mitjançant trucada o WhatsApp).</p>
            <h2>Responsable del tractament</h2>
            <p>Perruqueria D'Ara — {address}. Telèfon: {phone}.</p>
            <h2>Finalitat</h2>
            <p>Les dades facilitades (nom, telèfon) s'utilitzen únicament per gestionar la teva reserva o consulta.</p>
            <h2>Drets</h2>
            <p>Pots exercir els teus drets d'accés, rectificació i supressió posant-te en contacte amb nosaltres.</p>
            <p><em>Aquest text és un model de referència: recomanem revisar-lo amb una persona assessora legal abans de publicar-lo definitivament.</em></p>
            """.format(address=ADDRESS, phone=PHONE_DISPLAY),
        ),
        "avis-legal.html": (
            "Avís legal",
            """
            <p>Aquest lloc web és propietat de Perruqueria D'Ara, amb domicili a {address}.</p>
            <h2>Objecte</h2>
            <p>Aquest web té per objecte informar sobre els serveis de perruqueria oferts per D'Ara a Figueres.</p>
            <h2>Propietat intel·lectual</h2>
            <p>Els continguts, imatges i marca D'Ara són propietat de Perruqueria D'Ara i no es poden reproduir sense autorització.</p>
            <p><em>Aquest text és un model de referència: recomanem revisar-lo amb una persona assessora legal abans de publicar-lo definitivament.</em></p>
            """.format(address=ADDRESS),
        ),
        "cookies.html": (
            "Política de cookies",
            """
            <p>Aquest lloc web utilitza únicament les cookies tècniques necessàries per al seu correcte funcionament.</p>
            <h2>Què és una cookie</h2>
            <p>Una cookie és un petit fitxer que es desa al teu navegador per recordar informació sobre la teva visita.</p>
            <h2>Gestió</h2>
            <p>Pots configurar el teu navegador per bloquejar o eliminar les cookies en qualsevol moment.</p>
            <p><em>Aquest text és un model de referència: recomanem revisar-lo amb una persona assessora legal abans de publicar-lo definitivament.</em></p>
            """,
        ),
    }
    for filename, (title, content) in pages.items():
        body = """
  <section>
    <div class="wrap legal-doc">
      <h1>{title}</h1>
      {content}
    </div>
  </section>
""".format(title=title, content=content)
        write(filename, page_shell(
            title="{} — Perruqueria D'Ara".format(title),
            description="{} de Perruqueria D'Ara.".format(title),
            body=body,
        ))


if __name__ == "__main__":
    build_index()
    build_service_pages()
    build_contact()
    build_legal()
    print("Site generated at", ROOT)
