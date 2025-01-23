print("Programa en ejecución")

import qrcode

# Introduccimos el URL
texto = input("Introduce el URL: ").strip()

# Introduccimos el nombre que querramos para guardar el documento.
archivo = input("Introduce el nombre del archivo para guardar el QR: ").strip()

# En caso que no hayan añadido la extension se la añadimos nosotros
if not archivo.endswith(".jpg"):
    archivo += ".jpg"

# Creamos las dimensiones del QR
qr = qrcode.QRCode(box_size = 10, border = 4)

# Codificamos el QR
qr.add_data(texto)

# Creamos la imagen y la guardamos
image = qr.make_image(fill_color= "black", back_color="white")
image.save(archivo)

print(f"Codigo QR guardado como {archivo}")