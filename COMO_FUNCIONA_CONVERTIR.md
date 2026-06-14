# Cómo funciona `convertir.py`

Este script es el encargado de realizar la conversión de archivos utilizando MarkItDown.

## Objetivo

Cuando un usuario selecciona uno o más archivos y hace clic en **"Convertir a Markdown"**, Windows ejecuta este script.

El script recibe las rutas de los archivos seleccionados, utiliza MarkItDown para convertirlos a Markdown y genera un archivo `.md` junto al archivo original.

## Código completo

```python
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
```

## Flujo general

```text
Archivo seleccionado
        │
        ▼
Windows ejecuta convertir.py
        │
        ▼
MarkItDown procesa el archivo
        │
        ▼
Se genera contenido Markdown
        │
        ▼
Se guarda un archivo .md
```

## Importación de módulos

```python
import sys
import os
from markitdown import MarkItDown
```

### sys

Permite acceder a los argumentos enviados por Windows al ejecutar el script.

### os

Se utiliza para manipular rutas y nombres de archivos.

### MarkItDown

Es la librería responsable de convertir documentos a Markdown.

## Verificación de argumentos

```python
if len(sys.argv) < 2:
    sys.exit(1)
```

Cuando Windows ejecuta el script, envía la ruta del archivo seleccionado como argumento.

Por ejemplo:

```text
convertir.py documento.pdf
```

Si no se recibe ningún archivo, el programa termina inmediatamente.

## Creación del conversor

```python
md = MarkItDown()
```

Se crea una instancia de MarkItDown que será utilizada para procesar los archivos seleccionados.

## Procesamiento de archivos

```python
for archivo in sys.argv[1:]:
```

El script recorre todos los archivos recibidos.

Aunque actualmente el menú contextual envía un único archivo, el código está preparado para trabajar con múltiples archivos si en el futuro se amplía el registro de Windows.

## Generación del nombre de salida

```python
salida = os.path.splitext(archivo)[0] + ".md"
```

Ejemplos:

```text
manual.pdf      → manual.md
reporte.docx    → reporte.md
datos.xlsx      → datos.md
```

De esta forma el archivo Markdown queda junto al archivo original.

## Conversión a Markdown

```python
resultado = md.convert(archivo)
```

MarkItDown analiza el archivo y genera una representación estructurada en Markdown.

Dependiendo del formato, puede extraer:

- Texto
- Encabezados
- Listas
- Tablas
- Enlaces
- Información estructurada

## Escritura del archivo

```python
with open(salida, "w", encoding="utf-8") as f:
    f.write(resultado.text_content)
```

El contenido generado se guarda en un archivo `.md` utilizando codificación UTF-8.

Esto garantiza compatibilidad con caracteres especiales y múltiples idiomas.

## Manejo de errores

```python
except Exception:
    continue
```

Si ocurre un error durante la conversión de un archivo:

- El programa no se detiene.
- Ignora el archivo problemático.
- Continúa con el resto de los archivos.

Esto permite procesar lotes completos sin interrupciones.

## Resultado final

Al finalizar, el usuario obtiene un archivo Markdown en la misma carpeta que el documento original.

Ejemplo:

```text
Proyecto/
├── Manual.pdf
└── Manual.md
```

El archivo generado puede utilizarse para documentación, bases de conocimiento, sistemas RAG o para alimentar modelos de lenguaje como ChatGPT, Claude, Gemini o Llama.
