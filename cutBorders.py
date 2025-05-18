from PIL import Image
import os

# Parámetros
input_folder = "imagenes_originales"
output_folder = "imagenes_recortadas"
borde = 96  # tamaño del borde a recortar (en píxeles)

# Crear carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Procesar todas las imágenes
for nombre_archivo in os.listdir(input_folder):
    if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        ruta_imagen = os.path.join(input_folder, nombre_archivo)
        imagen = Image.open(ruta_imagen)
        
        ancho, alto = imagen.size
        # Definir la caja para recortar: (izquierda, arriba, derecha, abajo)
        caja = (borde, borde, ancho - borde, alto - borde)
        imagen_recortada = imagen.crop(caja)

        # Guardar imagen recortada
        ruta_guardado = os.path.join(output_folder, nombre_archivo)
        imagen_recortada.save(ruta_guardado)

print("Recorte completado.")
