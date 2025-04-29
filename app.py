from flask import Flask, render_template, request, send_file, redirect, url_for
from autocorrect.autocorrect import Speller
from io import BytesIO
import json
from stats import generar_estadisticas
from detectChange import highlight_correcciones

app = Flask(__name__)
spell = Speller(lang = 'es')

PATH_CORPUS = "./corpus/word_count.json"

def import_json(spell, path):
    with open(path, "r", encoding="utf-8") as f:
        cess_esp_data = json.load(f)
    spell = Speller(lang='es', nlp_data=cess_esp_data)
    return spell

spell = import_json(spell, PATH_CORPUS)

def validateForm(form):
    input_type = form.get('input_type')
    if input_type == 'text':
        texto = form.get('texto', '').strip()
        if not texto:
            raise ValueError("Debe ingresar un texto.")
        return texto
    elif input_type == 'file':
        archivo = request.files.get('archivo')
        if not archivo or archivo.filename == '':
            raise ValueError("Debe subir un archivo.")
        return archivo.read().decode('utf-8')
    else:
        raise ValueError("Tipo de entrada desconocido.")


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', texto_original = '', texto_corregido = '', error = '')

@app.route('/procesar', methods = ['POST'])
def procesar():
    try:
        texto_original = validateForm(request.form)
        texto_corregido = spell(texto_original)
        stats_data = generar_estadisticas(texto_original, texto_corregido)
        texto_corregido_resaltado = highlight_correcciones(texto_original, texto_corregido)
    except Exception as e:
        return render_template('index.html', texto_original='', texto_corregido='', error=str(e), stats=None)

    return render_template('index.html', 
                           texto_original = texto_original, 
                           texto_corregido = texto_corregido, 
                           texto_corregido_resaltado = texto_corregido_resaltado, 
                           error = '', stats=stats_data)

@app.route('/descargar', methods = ['POST'])
def descargar():
    texto_corregido = request.form.get('texto_corregido')
    buffer = BytesIO()
    buffer.write(texto_corregido.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment = True, download_name = 'texto_corregido.txt', mimetype = 'text/plain')

def corregir_texto(texto):
    return spell(texto)


if __name__ == '__main__':
    app.run(debug = True)