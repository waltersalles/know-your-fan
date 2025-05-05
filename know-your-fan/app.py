from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DATABASE = 'database/fans.json'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Garante que o arquivo JSON exista
if not os.path.exists(DATABASE):
    with open(DATABASE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cidade = request.form['cidade']
    interesses = request.form.getlist('interesses')
    eventos = request.form['eventos']

    # Validação do CPF (usando a função que já criamos)
    if not validar_cpf(cpf):
        return render_template('form.html', error="CPF inválido. Por favor, insira um CPF válido.")

    # Processar a imagem enviada e extrair texto usando OCR
    doc = request.files['documento']
    if doc:
        # Salvar o documento
        filename = doc.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        doc.save(filepath)

        # Realizar OCR no documento
        extracted_text = ocr_from_image(filepath)
        print("Texto extraído do documento:")
        print(extracted_text)

    data = {
        "nome": nome,
        "cpf": cpf,
        "cidade": cidade,
        "interesses": interesses,
        "eventos": eventos,
        "texto_extraido": extracted_text,
    }

    # Salvar dados no arquivo JSON
    with open(DATABASE, 'r+') as f:
        fans = json.load(f)
        fans.append(data)
        f.seek(0)
        json.dump(fans, f, indent=2)

    return render_template('confirm.html', fan=data)
@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cidade = request.form['cidade']
    interesses = request.form.getlist('interesses')
    eventos = request.form['eventos']

    # Validação do CPF (usando a função que já criamos)
    if not validar_cpf(cpf):
        return render_template('form.html', error="CPF inválido. Por favor, insira um CPF válido.")

    # Processar a imagem enviada e extrair texto usando OCR
    doc = request.files['documento']
    if doc:
        # Salvar o documento
        filename = doc.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        doc.save(filepath)

        # Realizar OCR no documento
        extracted_text = ocr_from_image(filepath)
        print("Texto extraído do documento:")
        print(extracted_text)

    data = {
        "nome": nome,
        "cpf": cpf,
        "cidade": cidade,
        "interesses": interesses,
        "eventos": eventos,
        "texto_extraido": extracted_text,
    }

    # Salvar dados no arquivo JSON
    with open(DATABASE, 'r+') as f:
        fans = json.load(f)
        fans.append(data)
        f.seek(0)
        json.dump(fans, f, indent=2)

    return render_template('confirm.html', fan=data)
@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cidade = request.form['cidade']
    interesses = request.form.getlist('interesses')
    eventos = request.form['eventos']

    # Validação do CPF (usando a função que já criamos)
    if not validar_cpf(cpf):
        return render_template('form.html', error="CPF inválido. Por favor, insira um CPF válido.")

    # Processar a imagem enviada e extrair texto usando OCR
    doc = request.files['documento']
    if doc:
        # Salvar o documento
        filename = doc.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        doc.save(filepath)

        # Realizar OCR no documento
        extracted_text = ocr_from_image(filepath)
        print("Texto extraído do documento:")
        print(extracted_text)

    data = {
        "nome": nome,
        "cpf": cpf,
        "cidade": cidade,
        "interesses": interesses,
        "eventos": eventos,
        "texto_extraido": extracted_text,
    }

    # Salvar dados no arquivo JSON
    with open(DATABASE, 'r+') as f:
        fans = json.load(f)
        fans.append(data)
        f.seek(0)
        json.dump(fans, f, indent=2)

    return render_template('confirm.html', fan=data)
@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cidade = request.form['cidade']
    interesses = request.form.getlist('interesses')
    eventos = request.form['eventos']

    # Validação do CPF (usando a função que já criamos)
    if not validar_cpf(cpf):
        return render_template('form.html', error="CPF inválido. Por favor, insira um CPF válido.")

    # Processar a imagem enviada e extrair texto usando OCR
    doc = request.files['documento']
    if doc:
        # Salvar o documento
        filename = doc.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        doc.save(filepath)

        # Realizar OCR no documento
        extracted_text = ocr_from_image(filepath)
        print("Texto extraído do documento:")
        print(extracted_text)

    data = {
        "nome": nome,
        "cpf": cpf,
        "cidade": cidade,
        "interesses": interesses,
        "eventos": eventos,
        "texto_extraido": extracted_text,
    }

    # Salvar dados no arquivo JSON
    with open(DATABASE, 'r+') as f:
        fans = json.load(f)
        fans.append(data)
        f.seek(0)
        json.dump(fans, f, indent=2)

    return render_template('confirm.html', fan=data)


if __name__ == '__main__':
    app.run(debug=True)
