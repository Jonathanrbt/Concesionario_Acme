from datetime import datetime
from modulos_acme.gestor_archivos import leer_archivos, escribir_archivos

def validar_cantidad(cantidad):
    return cantidad.isdigit() and int(cantidad) > 0

def solicitar_nuevo_codigo(ventas, codigo_actual):
    while codigo_actual in ventas:
        nuevo_codigo = input('''
╔═════════════════════════════════════════════════╗
║  SU CÓDIGO YA ES EXISTENTE EN LA BASE DE DATOS  ║
║                 (s). PARA SALIR                 ║
╚═════════════════════════════════════════════════╝

Ingrese un nuevo código: ''').strip()
        
        if nuevo_codigo == 's':
            return None
        codigo_actual = nuevo_codigo
    return codigo_actual

def crear_registro_venta(codigo, cantidad, fecha):
    return {
        'code': codigo,
        'Sales': cantidad,
        'fechaRegistrada': fecha
    }

def registro_ventas():
    try:
        # Inicializamos un diccionario vacío en caso de que no exista el archivo
        ventas = {}
        
        # Intentamos cargar las ventas existentes
        ventas_cargadas = leer_archivos('ventas_vehiculos')
        if isinstance(ventas_cargadas, dict):
            ventas = ventas_cargadas

        # Solicitar datos
        code = input("Ingrese el código del producto: ").strip()
        quanty = input("Ingrese la cantidad vendida: ").strip()

        # Validar cantidad
        if not validar_cantidad(quanty):
            print("Cantidad inválida. Ingrese un número positivo por favor.")
            return

        # Verificar si el código existe y solicitar uno nuevo si es necesario
        code = solicitar_nuevo_codigo(ventas, code)
        if code is None:
            return

        # Crear fecha actual
        fecha_actual = datetime.now()
        fecha = fecha_actual.strftime('%Y-%m-%d')

        # Crear el nuevo registro
        nuevo_registro = crear_registro_venta(code, quanty, fecha)
        
        # Actualizar el diccionario de ventas
        ventas[code] = nuevo_registro
        
        # Guardar los cambios
        escribir_archivos('ventas_vehiculos', ventas)
        
        print('\n¡Venta registrada con éxito!')
        
    except Exception as e:
        print(f"Error al procesar la venta: {str(e)}")