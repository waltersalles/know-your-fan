from flask import Flask, render_template, request
from validator import validar_cpf
from ocr_utils import extrair_texto

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mensagem = ""
    if request.method == 'POST':
        cpf = request.form['cpf']
        if not validar_cpf(cpf):
            mensagem = "CPF inválido!"
        else:
            documento = request.files['documento']
            texto = extrair_texto(documento)
            mensagem = f"OCR realizado! Detalhes extraídos: {texto[:100]}..."
    return render_template("index.html", mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
