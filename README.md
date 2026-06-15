# MarkItDown. Convertir archivos a Markdown con click derecho.

Agrega la opción **"Convertir a Markdown"** al menú de click derecho de Windows, utilizando [MarkItDown](https://github.com/microsoft/markitdown), una herramienta de código abierto desarrollada por Microsoft diseñada para transformar documentos complejos en texto Markdown limpio y estructurado.

Seleccionas uno o varios archivos, click derecho, y se convierten a Markdown automáticamente. Sin abrir programas, sin terminales, sin complicaciones.

---

## ¿Qué es MarkItDown?

MarkItDown es un convertidor universal de documentos que transforma una amplia variedad de formatos (PDF, Word, PowerPoint, Excel, imágenes, HTML, entre otros) en archivos Markdown.

A diferencia de los extractores de texto tradicionales, MarkItDown intenta preservar la estructura semántica del contenido, incluyendo:

- Títulos y subtítulos
- Listas numeradas y con viñetas
- Tablas
- Enlaces
- Código fuente
- Metadatos relevantes
- Organización jerárquica del documento

El resultado es un archivo Markdown fácil de leer tanto para humanos como para sistemas automatizados.

## ¿Por qué Markdown?

Los modelos de lenguaje (LLMs) como ChatGPT, Claude, Gemini, DeepSeek o Llama procesan mejor información estructurada que documentos binarios complejos como PDF o DOCX.

Markdown ofrece varias ventajas:

- Es texto plano, por lo que no requiere procesamiento adicional.
- Mantiene la estructura lógica del documento.
- Reduce el ruido generado por formatos propietarios.
- Facilita la indexación, búsqueda y fragmentación (chunking) de información.
- Mejora la calidad de los sistemas RAG (Retrieval-Augmented Generation).

## ¿Por qué MarkItDown es especialmente útil para LLMs?

Cuando se trabaja con grandes cantidades de documentación, uno de los mayores desafíos es convertir archivos heterogéneos en un formato que los modelos puedan entender eficientemente.

MarkItDown resuelve este problema al actuar como una capa de normalización de datos:

- Convierte múltiples formatos a una representación común.
- Conserva la jerarquía del contenido.
- Facilita la creación de bases de conocimiento.
- Simplifica la carga masiva de documentos en asistentes de IA.
- Reduce errores de interpretación causados por formatos complejos.

Por ejemplo, una carpeta que contiene manuales en PDF, presentaciones PowerPoint, hojas de cálculo Excel, documentos Word y archivos HTML puede convertirse completamente a Markdown para ser utilizada posteriormente por sistemas de búsqueda semántica, motores RAG o asistentes basados en LLMs.

Esto hace que MarkItDown sea especialmente valioso para estudiantes, investigadores, empresas y desarrolladores que necesitan entregar grandes volúmenes de información a modelos de inteligencia artificial de manera eficiente.

## ¿Qué hace este proyecto?

Este repositorio integra MarkItDown directamente en el menú de click derecho de Windows. En vez de usar la terminal cada vez, simplemente haces click derecho sobre un archivo y seleccionas **"Convertir a Markdown"**. El archivo `.md` aparece en la misma carpeta.

Por ejemplo, si tienes un archivo llamado `informe.pdf`, al hacer click derecho y seleccionar la opción aparecerá un nuevo archivo `informe.md` en la misma carpeta.

## Formatos compatibles

- PDF
- Word (.docx)
- Excel (.xlsx, .xls)
- PowerPoint (.pptx)
- HTML
- CSV
- JSON, XML
- Imágenes (extrae texto si lo tienen)
- ZIP (convierte los archivos dentro)

## ¿Qué necesito?

- Un computador con **Windows 10** o superior
- **Python 3.9** o superior (se explica cómo instalarlo más abajo)
- No se necesitan conocimientos de programación

---

## Instalación paso a paso

### Paso 1: Instalar Python

Si ya tienes Python instalado, puedes saltar al Paso 2.

1. Abre tu navegador y ve a [python.org/downloads](https://www.python.org/downloads/).
2. Descarga la versión más reciente para Windows.
3. Ejecuta el instalador.
4. **Muy importante:** marca la casilla **"Add Python to PATH"** que aparece abajo en la primera pantalla del instalador. Sin esto, los pasos siguientes no funcionarán.
5. Presiona **"Install Now"** y espera a que termine.

### Paso 2: Verificar que Python funciona

1. Abre **PowerShell** (búscalo en el menú Inicio escribiendo "PowerShell").
2. Escribe lo siguiente y presiona Enter:

```
python --version
```

3. Deberías ver algo como `Python 3.11.4` o similar. Si aparece un número de versión, Python está listo. Si da error, reinstala Python asegurándote de marcar "Add Python to PATH".

### Paso 3: Descargar este proyecto

Tienes dos opciones:

**Opción A: Descargar ZIP (más fácil)**

1. En esta misma página de GitHub, presiona el botón verde **"Code"**.
2. Selecciona **"Download ZIP"**.
3. Abre el ZIP descargado y extrae la carpeta en `C:\Users\TU_USUARIO\markitdown-menu\`.

> **¿Cómo sé cuál es mi nombre de usuario?** Abre PowerShell y escribe `echo $env:USERNAME`. Lo que aparezca es tu nombre de usuario.

**Opción B: Clonar con Git**

Si tienes Git instalado, abre PowerShell y ejecuta:

```
git clone https://github.com/ferjomendez/Markitdown-con-click-derecho.git
```

Luego renombra la carpeta descargada a `markitdown-menu` y muévela a `C:\Users\TU_USUARIO\`.

### Paso 4: Abrir PowerShell en la carpeta del proyecto

1. Abre la carpeta `markitdown-menu` en el Explorador de archivos.
2. Haz click en la barra de dirección (donde aparece la ruta), escribe `powershell` y presiona Enter. Esto abre PowerShell directamente en esa carpeta.

### Paso 5: Crear el entorno virtual

En la ventana de PowerShell que se abrió, escribe:

```
python -m venv .venv
```

Presiona Enter y espera unos segundos. No mostrará nada si todo salió bien.

> **¿Qué es un entorno virtual?** Es una instalación aislada de Python dentro de la carpeta del proyecto. Así no afecta nada más en tu computador y puedes borrarlo cuando quieras.

### Paso 6: Activar el entorno virtual

Escribe:

```
.venv\Scripts\activate
```

Si funcionó, verás `(.venv)` al inicio de la línea:

```
(.venv) PS C:\Users\TU_USUARIO\markitdown-menu>
```

> **¿Te da un error de permisos?** Ejecuta primero `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, responde "S" y vuelve a intentar.

### Paso 7: Instalar MarkItDown

Escribe:

```
pip install "markitdown[all]"
```

Esto descargará e instalará la herramienta y todas sus dependencias. Puede tardar unos minutos dependiendo de tu internet.

> Si aparece un aviso sobre `ffmpeg`, no te preocupes, eso solo afecta la conversión de archivos de audio. Todo lo demás funciona perfectamente.

### Paso 8: Configurar el menú de click derecho

1. Abre el archivo `instalar_menu.reg` haciendo click derecho sobre él y seleccionando **"Abrir con" → "Bloc de notas"**.
2. Verás varias veces el texto `TU_USUARIO`. Reemplázalo por tu nombre de usuario de Windows (el que obtuviste en el Paso 3).
3. Usa **Ctrl+H** (Buscar y reemplazar) para hacerlo rápido: busca `TU_USUARIO` y reemplaza por tu usuario.
4. Guarda el archivo con **Ctrl+S** y cierra el Bloc de notas.

### Paso 9: Registrar el menú contextual

1. Haz doble click sobre `instalar_menu.reg`.
2. Windows mostrará una advertencia preguntando si quieres modificar el Registro. Acepta.
3. Debería aparecer un mensaje confirmando que las claves se agregaron correctamente.

### Paso 10: Probar

1. Busca cualquier archivo PDF, Word, Excel o PowerPoint en tu computador.
2. Haz click derecho sobre él.
3. Deberías ver la opción **"Convertir a Markdown"**.
4. Haz click y espera unos segundos. Aparecerá un archivo `.md` con el mismo nombre en la misma carpeta.

Para convertir varios archivos a la vez, selecciónalos con Ctrl+Click, luego click derecho → **"Convertir a Markdown"**.

---

## Desinstalación

Si quieres eliminar la opción del menú de click derecho:

1. Presiona **Win + R**, escribe `regedit` y presiona Enter.
2. En la barra de navegación de la izquierda, busca: `HKEY_CLASSES_ROOT\*\shell`.
3. Dentro de `shell`, haz click derecho sobre la carpeta **"Convertir a Markdown"** y selecciona **Eliminar**.

Para eliminar la herramienta por completo, simplemente borra la carpeta `markitdown-menu`.

---

## Solución de problemas

**"python no se reconoce como un comando"**
Python no fue agregado al PATH. Reinstala Python y asegúrate de marcar la casilla "Add Python to PATH".

**No aparece la opción "Convertir a Markdown" al hacer click derecho**
- Verifica que ejecutaste el archivo `.reg` correctamente.
- Abre el `.reg` con el Bloc de notas y confirma que reemplazaste `TU_USUARIO` por tu nombre de usuario en todas las líneas.

**El archivo .md está vacío o tiene contenido extraño**
Algunos archivos pueden tener formatos que MarkItDown no interpreta completamente. Prueba con un documento más simple.

**Error de permisos al activar el entorno virtual**
Ejecuta en PowerShell: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a intentar.

---

## Créditos

Herramienta de conversión: [microsoft/markitdown](https://github.com/microsoft/markitdown)

Integración con menú contextual: [Fernando Méndez](https://github.com/ferjomendez)
