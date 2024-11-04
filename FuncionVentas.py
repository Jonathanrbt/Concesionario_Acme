import json  # Importa el módulo para trabajar con JSON
from datetime import datetime  # Importa la clase datetime para manejar fechas
import os  # Importa el módulo para interactuar con el sistema operativo

# Define el nombre del archivo JSON donde se guardarán las ventas
Base_ventas = "ventas.json"

# Función para registrar ventas
def registro_ventas():
    # Cargamos los datos existentes, si el archivo ya existe
    if os.path.exists(Base_ventas):
        with open(Base_ventas, 'r') as file:
            try:
                # Intentamos cargar los datos JSON existentes
                Ventas = json.load(file)
            except json.JSONDecodeError:
                # Si el archivo está vacío o tiene un error de formato, inicializamos un diccionario vacío
                Ventas = {}
    else:
        # Si el archivo no existe, inicializamos un diccionario vacío
        Ventas = {}

    # Ingresos por consola - inputs
    code = input("Ingrese el código del producto: ").strip()  # Solicita el código del producto
    quanty = input("Ingrese la cantidad vendida: ").strip()  # Solicita la cantidad vendida

    # Validar que la cantidad sea un número positivo
    if not quanty.isdigit() or int(quanty) <= 0:
        print("Cantidad inválida. Ingrese un número positivo por favor.")
        return  # Sale de la función si la cantidad no es válida

    # Creamos la fecha y hora actual
    fecha_actual = datetime.now()  # Obtiene la fecha y hora actuales
    fecha = fecha_actual.strftime('%Y-%m-%d')  # Formatea la fecha como cadena en el formato YYYY-MM-DD

    # Bucle para verificar si el código ya existe en las ventas
    while code in Ventas:
        # Solicita al usuario un nuevo código si ya existe
        codigo = input('''
╔═════════════════════════════════════════════════╗
║  SU CÓDIGO YA ES EXISTENTE EN LA BASE DE DATOS  ║
║                 (s). PARA SALIR                 ║
╚═════════════════════════════════════════════════╝

Ingrese un nuevo código: ''').strip()  # Pide un nuevo código
        if codigo == 's':
            # Si el usuario ingresa 's', sale de la función
            return
        code = codigo  # Actualiza el código con el nuevo valor ingresado

    # Agrega la nueva venta al diccionario Ventas
    Ventas[code] = {
        'codigo': code,
        'ventas': quanty,
        'fechaRegistrada': fecha  # Almacena la fecha como cadena
    }
    
    # Guardamos los datos ingresados en el archivo JSON
    with open(Base_ventas, 'w') as file:
        json.dump(Ventas, file, indent=4)  # Escribe el diccionario Ventas en el archivo, con indentación para legibilidad
    
    # Mensaje de éxito
    print('\n¡venta registrada con éxito!')
