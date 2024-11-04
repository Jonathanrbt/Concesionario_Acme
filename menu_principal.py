import time



def menu ():
    opcion = input('''
╔════════════════════════╗
║  GESTION DE VEHICULOS  ║
╚════════════════════════╝

(1). Registro de productos.
(2). Ingresar producto al inventario.
(3). Sacar productos del inventario.
(4). Buscar productos.
(0). Salir de programa.

Seleccione algunas de las opciones: ''')
    return opcion





while True:
    opc = menu()
    match opc:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '0':
            print('''
╔═══════════════════════════╗
║  FINALIZANDO PROGRAMA...  ║
╚═══════════════════════════╝''')
            time.sleep(2)
            break
        case _:
            print('''
╔═══════════════════════════════════════════╗
║   PORFAVOR SELECCIONE UNA OPCION VALIDA   ║
║ EL RANGO ESTA ENTRE (1-4). (0) PARA SALIR ║
╚═══════════════════════════════════════════╝''')