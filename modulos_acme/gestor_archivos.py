import json

def leer_archivos(opc):
    """
    Lee archivos JSON según la opción especificada
    """
    if opc == 'registro vehiculos':
        try:
            with open('registro_vehiculos.json', 'r') as file_registro:
                return json.load(file_registro)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    elif opc == 'ventas_vehiculos':  # Corregido el nombre de la opción
        try:
            with open('ventas_vehiculos.json', 'r') as file_Ventas:  # Corregido el nombre del archivo
                return json.load(file_Ventas)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    return {}

def escribir_archivos(opc, archivo):
    """
    Escribe archivos JSON según la opción especificada
    """
    if opc == 'registro vehiculos':
        with open('registro_vehiculos.json', 'w') as file_registro:
            json.dump(archivo, file_registro, indent=4)
            
    elif opc == 'ventas_vehiculos':  # Corregido el nombre de la opción
        with open('ventas_vehiculos.json', 'w') as file_ventas:
            json.dump(archivo, file_ventas, indent=4)
