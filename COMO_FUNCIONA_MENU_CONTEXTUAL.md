# Cómo funciona el menú contextual de Windows

Este proyecto agrega una nueva opción al menú de clic derecho de Windows llamada:

```text
Convertir a Markdown
```

Cuando el usuario selecciona esta opción, Windows ejecuta automáticamente el script `convertir.py`.

## ¿Qué es un archivo .reg?

Los archivos `.reg` permiten modificar el Registro de Windows.

El Registro es una base de datos interna donde Windows almacena configuraciones del sistema, incluyendo las opciones disponibles en el menú contextual.

Al ejecutar `instalar_menu.reg`, se crean las entradas necesarias para que aparezca la opción **Convertir a Markdown** al hacer clic derecho sobre un archivo.

## Estructura general

```text
Registro de Windows
        │
        ▼
Menú contextual
        │
        ▼
Convertir a Markdown
        │
        ▼
pythonw.exe
        │
        ▼
convertir.py
        │
        ▼
MarkItDown
        │
        ▼
Archivo .md
```

## Ubicación de la clave

```reg
HKEY_CLASSES_ROOT\*\shell\
```

El asterisco (`*`) indica que la opción aparecerá para cualquier tipo de archivo.

Gracias a esto es posible convertir:

- PDF
- Word
- Excel
- PowerPoint
- HTML
- CSV
- JSON
- XML
- Imágenes
- Cualquier otro formato soportado por MarkItDown

## Nombre mostrado en el menú

```reg
@="Convertir a Markdown"
```

Esta línea define el texto que verá el usuario.

Resultado:

```text
Convertir a Markdown
```

## Icono

```reg
"Icon"="..."
```

Permite mostrar un icono personalizado junto a la opción del menú.

Normalmente se utiliza el ejecutable de MarkItDown para que Windows extraiga automáticamente un icono.

## Selección múltiple

```reg
"MultiSelectModel"="Player"
```

Esta propiedad permite que la opción siga apareciendo cuando el usuario selecciona varios archivos simultáneamente.

## Comando ejecutado

La sección más importante del archivo es:

```reg
[HKEY_CLASSES_ROOT\*\shell\Convertir a Markdown\command]
```

Aquí se define exactamente qué debe ejecutar Windows.

Generalmente se utiliza un comando similar a:

```text
pythonw.exe convertir.py "%1"
```

## ¿Qué significa `%1`?

`%1` es un marcador especial que Windows reemplaza automáticamente por la ruta real del archivo seleccionado.

Por ejemplo:

```text
C:\Documentos\Manual.pdf
```

Por lo tanto Windows termina ejecutando algo equivalente a:

```text
pythonw.exe convertir.py "C:\Documentos\Manual.pdf"
```

## ¿Por qué usar `pythonw.exe`?

En lugar de utilizar:

```text
python.exe
```

se utiliza:

```text
pythonw.exe
```

porque:

- No abre una ventana de consola.
- La ejecución ocurre en segundo plano.
- La experiencia es más limpia para el usuario.

## Flujo completo

```text
Usuario hace clic derecho
            │
            ▼
Selecciona "Convertir a Markdown"
            │
            ▼
Windows lee el Registro
            │
            ▼
Ejecuta pythonw.exe
            │
            ▼
Lanza convertir.py
            │
            ▼
MarkItDown procesa el archivo
            │
            ▼
Genera archivo .md
```

## Desinstalación

Para eliminar la opción del menú contextual:

1. Abrir `regedit`.
2. Navegar a:

```text
HKEY_CLASSES_ROOT\*\shell\
```

3. Eliminar la carpeta:

```text
Convertir a Markdown
```

Una vez eliminada, la opción desaparece inmediatamente del menú contextual de Windows.

## Ventajas de esta implementación

- No requiere aplicaciones residentes en segundo plano.
- No modifica archivos originales.
- Funciona con cualquier formato soportado por MarkItDown.
- Se integra directamente con Windows.
- Permite convertir documentos con un solo clic.
- Es extremadamente ligera y fácil de mantener.
