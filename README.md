# Autocorrect + Flask

Implementacion de una aplicacion Flask que permite el ingreso de texto en un archivo con el extension apropiada. Se consigue que se corrijan faltas ortograficas en Español usando el corpus _cess_esp_.

Detecta y corrige errores de escritura. Esto suele implicar identificar palabras mal escritas, **compararlas con un corpus** de palabras correctas. Usando heuristica para la distancia de edicion.

## 1. Aplicación Flask

### Flujo de procesamiento del archivo

El flujo en la arquitectura cliente-servidor sería:

1. El usuario sube un archivo de texto (con palabras incompletas o con errores).
2. La aplicación Flask lee el contenido del archivo.
3. Se invoca la función de corrección que, utilizando el corpus `cess_esp` y las funciones de autocorrect [autocorrect](autocorrect/README.md), procesa el texto.
4. Se genera un nuevo archivo con el texto corregido y se devuelve al usuario.

## 2. Integración de Autocorrect con el corpus CESS-ESP

Adaptar la lógica del corrector para trabajar con el corpus CESS‑ESP implica:

- Generar un diccionario de frecuencias (JSON) directamente a partir de CESS‑ESP.
- Pasar este diccionario a la clase `Speller` mediante el argumento `nlp_data`, evitando así la descarga de la versión predeterminada.
- Revisar o ajustar, en caso necesario, las expresiones regulares y parámetros específicos para que coincidan con el contenido y estructura del corpus.

Esta integración te permitirá que el corrector "piense" con la estadística real de un corpus de referencia específico para el español, lo que puede mejorar notablemente la calidad de las correcciones en ese idioma.

### Aplicación en el proyecto

Este archivo obtenido al preprocesar conecta todos los componentes del corrector:

1. **Carga de datos:** Usa `load_from_tar` para obtener el diccionario de frecuencias.
2. **Corrección:** Utiliza `typos()` y `double_typos()` para generar candidatos y selecciona la mejor opción basada en frecuencia.
3. **Interfaz:** Permite corregir palabras y oraciones completas mediante la clase `Speller`.
