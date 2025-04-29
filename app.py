from flask import Flask, render_template, request, send_file, redirect, url_for
from autocorrect import Speller
from io import BytesIO

app = Flask(__name__)

spell = Speller(lang = 'es')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', texto_original = '', texto_corregido = '', error = '')

@app.route('/procesar', methods = ['POST'])
def procesar():
    input_type = request.form.get('input_type')
    texto_corregido = ""

    if input_type == 'text':
        texto = request.form.get('texto').strip()
        if not texto:
            return render_template('index.html', texto_original = '', texto_corregido = '', error = 'Debe ingresar un texto.')
        texto_original = texto
        texto_corregido = corregir_texto(texto)
    elif input_type == 'file':
        archivo = request.files.get('archivo')
        if not archivo or archivo.filename == '':
            return render_template('index.html', texto_original = '', texto_corregido = '', error = 'Debe subir un archivo.')
        contenido = archivo.read().decode('utf-8')
        texto_original = contenido
        texto_corregido = corregir_texto(contenido)
    else:
        return render_template('index.html', texto_original = '', texto_corregido = '', error = 'Error desconocido.')

    return render_template('index.html', texto_original = texto_original, texto_corregido = texto_corregido, error = '')

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