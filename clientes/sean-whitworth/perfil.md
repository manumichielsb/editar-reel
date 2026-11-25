# Perfil de cliente: The Law Offices of Sean R. Whitworth

Perfil de marca para `/editar-reel`. Solo branding y reglas de edición: **nunca** se guardan clips ni renders en el repo.

## Cliente
- Firma: **The Law Offices of Sean R. Whitworth** (abogado: **Sean R. Whitworth**, "Attorney Whitworth").
- Especialidad: **Divorce and Family Law**, flat fee ("One Fee, Quoted Upfront").
- Ubicación: Marietta, Georgia (Cobb County, North Metro Atlanta). En el State Bar of Georgia desde 2008.
- Web: https://www.seanwhitworth.com/ · Instagram: @lawofficesofseanwhitworth
- Paralegal: Michelle Cassell.

## Identidad visual (relevada de la web y la paleta del cliente)
| Uso | Color |
|---|---|
| Azul marino principal (paleta) | `#00287F` |
| Azul marino de la web (botones, fondos) | `#001973` |
| Gris | `#5E5E5E` |
| Blanco / negro | `#FFFFFF` / `#000000` |

- Tipografías de la web: Albert Sans (texto), Open Sans, Cormorant Garamond (titulares serif); el logo usa una serif
  de versalitas. En el reel se usan sus equivalentes incluidas en la skill: **Montserrat Bold** (subtítulos,
  sans limpia y contemporánea) y **DM Serif Display** (títulos, eco de la serif del logo).
- Logo: `assets/logo-white.png` (blanco, fondo transparente, 462x112, de la web) para poner sobre video;
  `assets/logo-color.jpg` (azul sobre blanco) para fondos claros. **Nunca deformar, recolorear ni recortar**:
  escalar siempre proporcional (solo `w`), con aire alrededor.

## Look de edición
- Profesional, moderno, elegante, minimalista. Subtítulos blancos con sombra suave; los destacados en
  MAYÚSCULA sobre una píldora azul marino `#00287F` (blanco sobre azul se lee en cualquier fondo).
- Un destacado cada 6-10 s, solo términos clave (custody, child support, flat fee, alimony...). Menos es más.
- Animación suave (`soft`), sin rebotes ni inclinaciones. Zooms sutiles (1.0 / 1.15-1.2), sin flashes blancos.
- **Nada de:** emojis, stickers, `scribble`, brillitos, `light` de color, grade `cine`/`film`, transiciones
  exageradas. Efectos de sonido al mínimo (`sfx.gain` 0.35, sin pop en destacados; como mucho un whoosh suave
  en un corte a pantalla completa).
- B-roll de stock sobrio (oficinas, documentos, familias, tribunales genéricos), sin logos ni caras reconocibles
  de terceros. Escenas `stat`/`text`/`checklist` con acento `#00287F`.
- Cierre: **opcional, nunca automático**. Solo se agrega si la persona lo pide para ese reel. Si lo pide:
  minimalista y profesional, el logo blanco (`assets/logo-white.png`) centrado sobre el video oscurecido, o la tarjeta
  `profile` con nombre y usuario. **Nunca** seguidores, publicaciones ni seguidos (no pasar `followers`, `posts`
  ni `following`), sin sonidos de "Seguir" (`sfx: null`).
- Entrega: MP4 1080x1920 (la copia `-celu.mp4` de `check.py`); el 4K queda disponible si se pide.

## Idioma y contenido
- Audio y subtítulos en **inglés estadounidense** (`"language": "en"`). Ortografía US (counseling, favor...).
- Terminología a respetar: divorce, contested / uncontested divorce, child custody (legal / physical custody),
  visitation, parenting time, child support, modification, alimony, legitimation, contempt of court,
  protective order, prenuptial agreement, flat fee, consultation, State of Georgia, Cobb County.
- `--prompt` sugerido para Whisper: `Sean R. Whitworth, Whitworth, Marietta, Georgia, Cobb County, alimony,
  legitimation, prenuptial, contempt of court, protective order, flat fee, Michelle Cassell`.
- **Nunca** agregar información legal, afirmaciones ni promesas que Sean no dijo. Los textos en pantalla salen
  de sus palabras. No tocar su cara ni su voz, ni cambiar el sentido de lo que dice.
