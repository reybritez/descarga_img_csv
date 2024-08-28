import os
import requests
import csv

# Definir el server URL and la carpeta para guardar las imagenes
server_url = "http://192.168.x.x:PORT/"
save_folder = "download/"
# Crea la carpeta si no existe
os.makedirs(save_folder, exist_ok=True)

# Lee el csv

with open('images.csv', mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        name, url_route = row
        # Limpiar el nombre del archivo
        name = name.strip().strip('"')  # Eliminar espacios y comillas
        name = ''.join(c for c in name if c.isalnum() or c in ('-', '_'))  # Mantener solo caracteres alfanuméricos, guiones y guiones bajos
        full_url = server_url + url_route.strip()
        response = requests.get(full_url)
        if response.status_code == 200:
            # Extraer la extensión del archivo de la URL
            _, extension = os.path.splitext(url_route)
            # Crear el nombre del archivo con la extensión correcta
            image_path = os.path.join(save_folder, f"{name}{extension}")
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Imagen guardada: {image_path}")
        else:
            print(f"No se pudo descargar la imagen: {full_url}")