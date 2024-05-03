import os
from PyPDF2 import PdfReader

# Especifique o caminho para o arquivo PDF
pdf_path = 'abc.pdf'

# Verifique se o arquivo existe
if os.path.exists(pdf_path):
    # Abra o arquivo PDF
    with open(pdf_path, 'rb') as file:
        # Crie um objeto leitor de PDF
        pdf_reader = PdfReader(file)
        # Obtenha o texto da primeira página
        page = pdf_reader.pages[0]
        text = page.extract_text()
        # Divida o texto em palavras
        words = text.split()
        # Imprima as primeiras 10 palavras
        print(words[:10])
else:
    print("Arquivo PDF não encontrado.")
    
    