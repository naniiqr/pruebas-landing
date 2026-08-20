# Perruqueria D'Ara — Sitio web

Sitio estático (HTML + CSS + JS, sin build ni dependencias) generado a partir del PDF de referencia. Listo para publicarse en GitHub Pages.

## Estructura

```
index.html                                  Inici
talls-i-canvi-destil.html                   Servei
pentinats.html                               Servei
tractaments-de-recuperacio-capillar.html     Servei
tecniques-de-color-tints-i-metxes.html       Servei
allisats-organics.html                       Servei
pentinats-de-nuvia.html                       Servei
situacio-i-contacte.html                      Contacte
privacitat.html / avis-legal.html / cookies.html   Legal (textos modelo — revisar con asesoría legal)
css/style.css                                 Estilos y sistema de diseño
js/main.js                                    Menú móvil + animaciones al hacer scroll
images/                                       Fotos reales del salón (extraídas del PDF)
```

Todas las rutas son relativas, así que el sitio funciona igual en local, en un subdirectorio o en la raíz de un dominio — no requiere configuración especial.

## Publicar en GitHub Pages (repositorio "landing")

**Opción A — subir desde la web de GitHub (sin instalar nada):**

1. Entra en [github.com/new](https://github.com/new) y crea un repositorio público llamado `landing`.
2. Abre el repo → botón **Add file → Upload files**.
3. Arrastra **todo el contenido de esta carpeta** (no la carpeta en sí, sino lo que hay dentro: `index.html`, `css/`, `js/`, `images/`, etc.) y haz commit.
4. Ve a **Settings → Pages**.
5. En "Build and deployment" → Source: **Deploy from a branch**. Branch: **main**, carpeta **/ (root)**. Guarda.
6. En 1–2 minutos el sitio estará en `https://<tu-usuario>.github.io/landing/`.

**Opción B — con git desde tu ordenador:**

```bash
cd landing               # carpeta donde has descargado estos archivos
git init
git add .
git commit -m "Sitio web D'Ara Perruqueria"
git branch -M main
git remote add origin https://github.com/<tu-usuario>/landing.git
git push -u origin main
```

Luego activa Pages igual que en el paso 4–5 de la Opción A.

## Notas antes de publicar

- **Mapa**: el bloque de "Situació i contacte" usa un iframe de Google Maps con la dirección ya escrita (Carrer Méndez Núñez, 41, Figueres). Funciona directamente en cuanto el sitio esté en un dominio real; en este entorno de pruebas puede no cargar por restricciones de red del sandbox.
- **WhatsApp**: el botón flotante y los CTA apuntan a `wa.me/34972672827` (el mismo teléfono del negocio). Cambia el número en `build.py` (constante `WHATSAPP_NUMBER`) si el WhatsApp de reservas es distinto al fijo.
- **Horarios**: no había horario de apertura en el PDF original, así que la página de contacto dice "amb cita prèvia" en vez de inventar un horario. Si quieres horarios concretos, dímelo y los añado.
- **Textos legales**: `privacitat.html`, `avis-legal.html` y `cookies.html` son textos modelo genéricos — conviene que los revise una gestoría o asesoría legal antes de publicarlos definitivamente.
- **Regenerar el sitio**: todo el contenido (textos, teléfonos, imágenes de cada servicio) vive en `_generator/build.py`. Edita ese archivo y ejecuta `python3 build.py` desde dentro de `_generator/` (copiando antes las carpetas `css/`, `js/` e `images/` a su lado, o ajustando la variable `ROOT`) para regenerar todos los HTML de golpe sin tener que tocarlos uno a uno. Esta carpeta no hace falta subirla a GitHub Pages — es solo para mantenimiento futuro.
