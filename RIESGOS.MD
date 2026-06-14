# Seguridad y Riesgos

Una de las preguntas más comunes al instalar herramientas que modifican el menú contextual de Windows es si representan algún riesgo para el sistema.

La respuesta corta es: **los riesgos reales son mínimos**, pero siempre es recomendable entender qué hace exactamente el software que estamos ejecutando.

## ¿Qué hace este proyecto?

Este proyecto consta únicamente de dos componentes:

1. Un archivo `.reg` que agrega una opción al menú contextual de Windows.
2. Un script de Python (`convertir.py`) que utiliza MarkItDown para convertir documentos a Markdown.

No instala servicios, no modifica configuraciones avanzadas del sistema y no envía información a internet.

---

## Riesgo 1: Modificaciones del Registro de Windows

El componente más delicado del proyecto es el archivo `instalar_menu.reg`.

Los archivos `.reg` tienen la capacidad de modificar el Registro de Windows, por lo que siempre deben revisarse antes de ejecutarlos, especialmente si provienen de una fuente desconocida.

En este proyecto, el archivo `.reg` únicamente:

- Agrega una entrada al menú contextual.
- Define el icono que se mostrará.
- Indica qué comando ejecutar al hacer clic.

No modifica configuraciones de seguridad, permisos, red ni componentes críticos del sistema operativo.

### Recomendación

Antes de ejecutar cualquier archivo `.reg` descargado de internet:

1. Ábrelo con el Bloc de notas.
2. Revisa su contenido.
3. Verifica que las rutas y comandos sean los esperados.

---

## Riesgo 2: Acceso a archivos locales

El script `convertir.py` necesita leer los archivos seleccionados para poder convertirlos.

Sin embargo:

- Solo accede a los archivos que el usuario selecciona explícitamente.
- No recorre carpetas automáticamente.
- No modifica el archivo original.
- No elimina archivos.
- No realiza cambios fuera de la carpeta donde se genera el archivo Markdown.

Su comportamiento es completamente local.

Por ejemplo:

```text
Manual.pdf
```

genera:

```text
Manual.md
```

sin alterar el PDF original.

---

## Riesgo 3: Conexión a internet

Ninguno de los componentes de este proyecto envía información a internet.

La conversión ocurre completamente en el equipo del usuario.

No existen:

- Subidas de archivos.
- Servicios en la nube.
- APIs externas.
- Telemetría propia del proyecto.

Todo el procesamiento ocurre localmente.

---

## Riesgo 4: Dependencias externas

La conversión es realizada por MarkItDown.

MarkItDown es:

- Un proyecto Open Source.
- Desarrollado por Microsoft.
- Con código fuente público.
- Revisado continuamente por la comunidad.

Repositorio oficial:

https://github.com/microsoft/markitdown

Como cualquier dependencia de terceros, siempre es recomendable instalarla desde fuentes oficiales.

---

## Riesgo 5: Archivos maliciosos

El escenario de riesgo más realista no proviene de este proyecto, sino de los archivos que se intentan convertir.

Por ejemplo:

- PDFs especialmente diseñados para explotar vulnerabilidades.
- Documentos corruptos.
- Archivos manipulados de forma maliciosa.

Este riesgo existe en cualquier software que procese documentos, incluyendo navegadores, lectores PDF y suites ofimáticas.

Además, sería una vulnerabilidad de las librerías de procesamiento utilizadas internamente, no del proyecto en sí.

La probabilidad es extremadamente baja, pero nunca puede considerarse cero.

---

## Riesgo 6: Archivo .reg modificado por terceros

Otro escenario posible es que alguien modifique el archivo `.reg` antes de que sea ejecutado.

Por ejemplo, podría cambiar la ruta del comando para ejecutar un programa distinto al esperado.

Por esta razón se recomienda:

- Descargar el proyecto desde su repositorio oficial.
- Revisar el contenido del archivo `.reg`.
- Evitar ejecutar versiones obtenidas de fuentes desconocidas.

Mantener el código en un repositorio público permite que cualquier persona pueda inspeccionarlo y verificar exactamente qué hace.

---

## Buenas prácticas recomendadas

- Descargar siempre desde el repositorio oficial.
- Revisar el contenido del archivo `.reg` antes de ejecutarlo.
- Mantener Python y las dependencias actualizadas.
- Utilizar un antivirus actualizado.
- No convertir archivos provenientes de fuentes sospechosas.

---

## Conclusión

Para un usuario normal, este proyecto presenta un nivel de riesgo muy bajo.

El archivo `.reg` únicamente agrega una opción al menú contextual, el script de Python trabaja localmente y MarkItDown es una librería Open Source ampliamente utilizada.

Siempre existe un riesgo teórico asociado a ejecutar software o procesar documentos externos, pero dentro de un uso normal y siguiendo buenas prácticas básicas, no hay motivos razonables de preocupación.
