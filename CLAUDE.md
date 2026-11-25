# Notas para Claude

- La skill `/editar-reel` se usa desde un iPad en la nube: los clips llegan subidos al chat y los MP4 terminados se
  le mandan a la persona como archivo (SendUserFile). La skill instalada vive en `~/.claude/skills/editar-reel`.
- La persona es Social Media Manager con varios clientes. Antes de editar, preguntá (si no lo dice) para qué
  cliente es y activá su perfil: `bash clientes/usar.sh <cliente>`; leé `clientes/<cliente>/perfil.md` y aplicá
  `clientes/<cliente>/reel-defaults.json` en cada `reel.json`. Nunca mezcles el branding de un cliente con otro.
- Nunca subas clips, renders ni datos privados de clientes al repo: solo perfiles de branding.
