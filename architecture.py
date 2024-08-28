import os

# Definir la estructura de directorios y archivos
structure = {
    "domain/":["transcriber.py","transcription_service.py"],
    "domain/ports":["transcriber_port.py","storage_port.py"],
    "adapters/":["transcriber_adapter.py","storage_adapter.py","flask_api_adapter.py"]
}


# Crear las carpetas y los archivos
for folder, files in structure.items():
    # Crear la carpeta si no existe
    os.makedirs(folder, exist_ok=True)
    print(f"Carpeta creada: {folder}")

    # Crear los archivos .py
    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'w') as f:
            f.write("# " + file.split('.')[0].replace('_', ' ').title() + " Module\n")
        print(f"Archivo creado: {file_path}")

print("Estructura de carpetas y archivos creada correctamente.")
