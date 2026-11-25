# Notas para Claude

- La skill `/editar-reel` se usa desde un iPad en la nube: los clips llegan subidos al chat y los MP4 terminados se
  le mandan a la persona como archivo (SendUserFile). La skill instalada vive en `~/.claude/skills/editar-reel`.
- La persona es Social Media Manager con varios clientes. Antes de editar, preguntá (si no lo dice) para qué
  cliente es y activá su perfil: `bash clientes/usar.sh <cliente>`; leé `clientes/<cliente>/perfil.md` y aplicá
  `clientes/<cliente>/reel-defaults.json` en cada `reel.json`. Nunca mezcles el branding de un cliente con otro.
- Nunca subas clips, renders ni datos privados de clientes al repo: solo perfiles de branding.
- Clips grandes en Google Drive: si el archivo está compartido por link, bajalo con curl desde
  `drive.usercontent.google.com` (ver `clientes/*/perfil.md`); el conector de Drive no sirve para cientos de MB.
- Hyperframes en la nube: necesita `ONNXRUNTIME_NODE_INSTALL_CUDA=skip`, `ONNXRUNTIME_NODE_INSTALL=skip` y
  `HYPERFRAMES_BROWSER_PATH` (chrome-headless-shell de /opt/pw-browsers); el entorno "editar-reel" ya las define.
  `snap.py` a veces no dibuja las píldoras de los destacados: confirmá en un cuadro del render real.
- Entregas en 1080x1920: `render --resolution portrait` (más rápido que 4K en la nube); el aviso de 4K de
  `check.py` es esperado.
