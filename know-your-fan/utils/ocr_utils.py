import pytesseract
from PIL import Image
import tempfile

def extrair_texto(file_storage):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        file_storage.save(tmp.name)
        imagem = Image.open(tmp.name)
        return pytesseract.image_to_string(imagem)
