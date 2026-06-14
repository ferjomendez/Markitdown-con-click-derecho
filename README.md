# MarkItDown. Menú contextual para Windows

Agrega la opción **"Convertir a Markdown"** al menú de click derecho de Windows, usando [MarkItDown](https://github.com/microsoft/markitdown) de Microsoft.

Soporta conversión individual y selección múltiple de archivos.

## ¿Qué es MarkItDown?

MarkItDown es una herramienta de código abierto desarrollada por Microsoft que convierte documentos y archivos de múltiples formatos a **Markdown**, un formato de texto ligero ampliamente utilizado para documentación técnica, bases de conocimiento y aplicaciones de inteligencia artificial.

A diferencia de extractores de texto tradicionales, MarkItDown intenta preservar la estructura semántica del contenido, incluyendo títulos, listas, tablas, enlaces, fragmentos de código y otros elementos importantes. Esto permite obtener documentos mucho más limpios y fáciles de procesar posteriormente.

## ¿Por qué Markdown?

Markdown es un formato de texto plano que mantiene la estructura lógica de un documento sin depender de formatos propietarios como PDF, DOCX o PPTX. Esto facilita:

- La lectura y edición por personas.
- El procesamiento automático por software.
- La indexación y búsqueda de información.
- La creación de documentación portable y duradera.

## ¿Por qué es útil para LLMs e Inteligencia Artificial?

Los modelos de lenguaje modernos (LLMs) como ChatGPT, Claude, Gemini, DeepSeek o Llama trabajan mejor cuando reciben información estructurada y libre de ruido de formato.

MarkItDown se ha vuelto especialmente popular porque permite transformar grandes colecciones de documentos a un formato que los modelos pueden interpretar de forma mucho más eficiente.

Entre sus ventajas destacan:

- Convierte múltiples formatos a una representación común.
- Conserva la jerarquía y organización del contenido.
- Reduce errores producidos por formatos complejos.
- Facilita el chunking (fragmentación de documentos).
- Mejora la calidad de sistemas RAG (Retrieval-Augmented Generation).
- Simplifica la construcción de bases de conocimiento para asistentes de IA.

Por ejemplo, una carpeta con manuales PDF, documentos Word, presentaciones PowerPoint, planillas Excel y archivos HTML puede convertirse completamente a Markdown para posteriormente alimentar un sistema de búsqueda semántica o un asistente basado en LLMs.

Esta capacidad de normalizar grandes volúmenes de información hace que MarkItDown sea una excelente herramienta para estudiantes, investigadores, desarrolladores y empresas que trabajan con inteligencia artificial.

## Formatos compatibles

PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx), imágenes, HTML, CSV, JSON, XML, ZIP, entre otros.

## Requisitos

- Windows 10 o superior
- Python 3.9 o superior

## Instalación

### 1. Instalar Python

Descarga Python desde [python.org](https://www.python.org/downloads/) si aún no lo tienes.

### 2. Crear un entorno virtual

Abre PowerShell y ejecuta:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar MarkItDown

```powershell
pip install 'markitdown[all]'
```

### 4. Clonar o descargar este repositorio

Coloca los archivos en `C:\Users\TU_USUARIO\markitdown-menu\`:

```
C:\Users\TU_USUARIO\markitdown-menu\
├── convertir.py
├── instalar_menu.reg
└── README.md
```

### 5. Editar el archivo `.reg`

Abre `instalar_menu.reg` con el Bloc de notas y reemplaza **todas** las ocurrencias de `TU_USUARIO` con tu nombre de usuario de Windows.

### 6. Registrar el menú contextual

Haz doble click en `instalar_menu.reg`, acepta el aviso de UAC y confirma la importación.

### 7. Probar

Click derecho sobre cualquier archivo compatible → **"Convertir a Markdown"**.

El archivo `.md` se guarda en la misma carpeta que el archivo original, con el mismo nombre.

## Uso

### Archivo individual

Click derecho sobre un archivo → **Convertir a Markdown**.

### Múltiples archivos

Selecciona varios archivos con `Ctrl+Click` o `Shift+Click`, click derecho → **Convertir a Markdown**. Se convierten todos de una vez.

## Desinstalar

Para eliminar la opción del menú contextual, abre el **Editor del Registro** (`regedit`), navega a:

```
HKEY_CLASSES_ROOT\*\shell\
```

Y elimina la carpeta **"Convertir a Markdown"**.

## Notas

- Al instalar con `markitdown[all]` puede aparecer un aviso sobre `ffmpeg`. No es un error, solo significa que la conversión de archivos de **audio** no estará disponible. Todos los demás formatos funcionan con normalidad.
- El script usa `pythonw.exe` para que la conversión ocurra en segundo plano, sin abrir una ventana de terminal.

## Créditos

Basado en [microsoft/markitdown](https://github.com/microsoft/markitdown).
