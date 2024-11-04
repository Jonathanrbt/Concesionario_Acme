def leer_archivos (opc):
    if opc == 'registro vehiculos':
        try:
            with open('registro_vehiculos.json', 'r') as file_registro:
                return json.load(file_registro)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}