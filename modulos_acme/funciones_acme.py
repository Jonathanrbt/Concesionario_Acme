from modulos_acme.gestor_archivos import *
from datetime import datetime


def registrar_vehiculos():
    vehiculos = leer_archivos('registro vehiculos')
    codigo = input('''
╔══════════════════════╗
║  REGISTRAR VEHICULO  ║
╚══════════════════════╝

Ingrese el codigo de su nuevo vehiculo: ''').strip()
    marca = input('Ingrese la marca de su nuevo vehiculo: ').strip()
    modelo = input('Ingrese el modelo de su nuevo vehiculo: ').strip()
    try:
        anio = int(input('Ingrese el año de lanzamiento de su nuevo vehiculo: '))
        if 1000 <= anio <= 9999:
            pass
        else:
            print('''
╔════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR UN AÑO CORRECTO!!║
╚════════════════════════════════════════╝''')
            return
    except ValueError:
        print('''
╔════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR UN AÑO CORRECTO!!║
╚════════════════════════════════════════╝''')
        return
    if codigo == '' or marca == '' or modelo == '' or anio == '':
        print('''
╔═════════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR AL MENOS UN CARACTER!!║
╚═════════════════════════════════════════════╝''')
    else:
        while codigo in vehiculos:
            codigo = input('''
╔═════════════════════════════════════════════════╗
║  SU CODIGO YA ES EXISTENTE EN LA BASE DE DATOS  ║
║                 (s). PARA SALIR                 ║
╚═════════════════════════════════════════════════╝

Ingrese un nuevo codigo: ''')
            if codigo == 's':
                return
            if codigo == '' or marca == '' or modelo == '' or anio == '':
                print('''
╔═════════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR AL MENOS UN CARACTER!!║
╚═════════════════════════════════════════════╝''')
                continue
        vehiculos[codigo] = {
            'marca': marca,
            'modelo': modelo,
            'fecha': anio
        }
        escribir_archivos('registro vehiculos', vehiculos)
        print('\n¡Su vehiculo fue creado con exito!')