def leer_archivos(opc):
    if opc == 'registro vehiculos':
        try:
            with open('registro_vehiculos.json', 'r') as file_registro:
                return json.load(file_registro)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}




def escribir_archivos(opc, archivo):
    if opc == 'registro vehiculos':
        with open('registro_vehiculos.json', 'w') as file_registro:
            json.dump(archivo, file_registro, indent=4)