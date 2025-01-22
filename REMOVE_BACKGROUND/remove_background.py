print("El programa está en ejecución")
print("Solo admite archivos .jpg, .jpeg, .png y .webp")
print("Buscando imágenes...")

# Cargamos las librerías
import os
from rembg import remove
from PIL import Image

# Creamos los directorios 
working_dir = os.getcwd()
input_dir = working_dir
output_dir = os.path.join(working_dir, "Fondo Removido")
formatos = (".jpg", ".jpeg", ".png", ".webp")

# Inicializamos los contadores
total_images = 0
procesadas = 0

# Contamos las imágenes
for filename in os.listdir(input_dir):
    if filename.endswith(formatos):
        total_images += 1

print(f"Total de imágenes: {total_images}")

# Creamos la carpeta si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Carpeta creada 'Fondo Removido'")

# Procesamos cada imagen que haya en la carpeta 
for filename in os.listdir(input_dir):
    if filename.endswith(formatos):
        try:
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"sin_fondo_{filename}")

            input_image = Image.open(input_path)
            output_image = remove(input_image)

            # Convertimos a RGB si el modo es RGBA (jpeg)
            if output_image.mode == "RGBA":
                output_image = output_image.convert("RGB")

            output_image.save(output_path)

            procesadas += 1

            print(f"¡El fondo de {filename} ha sido editado con éxito!")
            print(f"Imágenes procesadas: {procesadas} de {total_images}")
        except Exception as e:
            print(f"Error procesando la imagen {filename}: {e}")

print("¡Todas las imágenes han sido procesadas!")

# Pausa para evitar que la ventana del CMD se cierre automáticamente
input("Presiona cualquier tecla para salir...")
