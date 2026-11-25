#!/usr/bin/env bash
# Activa el perfil de un cliente para /editar-reel: bash clientes/usar.sh <cliente>
set -euo pipefail
dir="$(cd "$(dirname "$0")" && pwd)/${1:?Uso: usar.sh <cliente>}"
[ -f "$dir/config.json" ] || { echo "No existe el perfil: $dir"; exit 1; }
sk="${SK:-$HOME/.claude/skills/editar-reel}"
cp "$dir/config.json" "$sk/config.json"
python3 - "$dir/config.json" <<'P'
import json, os, sys
c = json.load(open(sys.argv[1]))
for k in ('clipsDir', 'projectsDir'):
    os.makedirs(os.path.expanduser(c[k]), exist_ok=True)
print('PERFIL', c['name'], '| clips:', c['clipsDir'], '| proyectos:', c['projectsDir'])
P
