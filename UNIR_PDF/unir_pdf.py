from PyPDF2 import PdfFileMerger, PdfFileReader
import os

# Obtener el directorio actual
directorio_actual = os.getcwd()

# Listar archivos PDF en el directorio actual
listaPdfs = os.listdir(directorio_actual)

# Crear el objeto PdfFileMerger
merger = PdfFileMerger()

# Agregar archivos PDF a la fusión
for file in listaPdfs:
    if file.endswith('.pdf'):  # Asegurarse de que el archivo es un PDF
        merger.append(PdfFileReader(os.path.join(directorio_actual, file)))

# Escribir el PDF fusionado en el directorio actual
merger.write(os.path.join(directorio_actual, 'PdfFinal.pdf'))
