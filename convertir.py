import sys
import os
from markitdown import MarkItDown

if len(sys.argv) < 2:
    sys.exit(1)

md = MarkItDown()

for archivo in sys.argv[1:]:
    try:
        salida = os.path.splitext(archivo)[0] + ".md"
        resultado = md.convert(archivo)
        with open(salida, "w", encoding="utf-8") as f:
            f.write(resultado.text_content)
    except Exception:
        continue
