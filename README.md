Know Your Fan (KYC FURIOSO)
📌 Descrição
O "Know Your Fan" é uma solução de verificação de identidade pensada para fãs da FURIA. O usuário envia seu CPF e uma imagem de documento, e o sistema realiza:

Validação do CPF com lógica nativa

Leitura do documento via OCR (Tesseract)

Interface estilizada com a estética FURIA

Resposta com resultado da extração

🚀 Funcionalidades
Upload de documento (imagem)

Validação precisa de CPF

Leitura de texto OCR da imagem enviada

Interface estilizada com visual da FURIA

Preparado para integração com banco de dados ou IA

🛠️ Tecnologias Utilizadas
Python 3.10+

Flask

Tesseract OCR (pytesseract)

Pillow

HTML + CSS

🔧 Como Rodar Localmente
Clone o repositório:

git clone(https://github.com/waltersalles/know-your-fan/)
cd kyc-furia
Instale as dependências:

pip install flask pillow pytesseract
⚠️ Você também precisa instalar o Tesseract OCR:

Windows: baixe o instalador .exe e adicione o caminho ao PATH.

Linux: sudo apt install tesseract-ocr

Mac: brew install tesseract

Rode a aplicação:
python app.py
Acesse:
http://127.0.0.1:5000

