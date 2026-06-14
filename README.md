# MarkItDown. Menú contextual para Windows

Agrega la opción **"Convertir a Markdown"** al menú de click derecho de Windows, usando [MarkItDown](https://github.com/microsoft/markitdown) de Microsoft.

Soporta conversión individual y selección múltiple de archivos.

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
