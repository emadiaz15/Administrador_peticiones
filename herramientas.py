# Importar funciones para los métodos de búsqueda desde un módulo externo
from metodos_peticiones import SSTF, scanA, scanB, scanCircular

# Decorador gráfico para imprimir separadores
def separadorLineas(char):
    separador = char * 50
    print(separador)

# Función que define el método de búsqueda
def buscar(listaOriginal, metodo, actual):
    lista = listaOriginal.copy()  # Hacemos una copia de la lista original

    # Implementación de los métodos de búsqueda
    if metodo == 1:
        return SSTF(lista, actual)
    elif metodo == 2:
        return scanA(lista, actual)
    elif metodo == 3:
        return scanB(lista, actual)
    elif metodo == 4:
        return scanCircular(lista, actual)

# Función para calcular el total de movimientos
def totalMovimientos(lista, posicionInicial):
    total = abs(posicionInicial - lista[0])

    for i in range(1, len(lista)):
        movimiento = abs(lista[i - 1] - lista[i])
        total += movimiento

    return total

# Función para validar la entrada del usuario y seleccionar un método de búsqueda
def validacionInput():
    print('Pulse 1 para SSTF')
    print('Pulse 2 para Scan por mayores primero')
    print('Pulse 3 para Scan por menores primero')
    print('Pulse 4 para Scan circular')
    operacionesValidas = [1, 2, 3, 4]
    
    while True:
        try:
            operacion = int(input('Seleccione el método: '))
            if operacion in operacionesValidas:
                return operacion
            else:
                print('Opción no válida. Por favor, elija una opción válida (1, 2, 3 o 4).')
        except ValueError:
            print('Entrada no válida. Por favor, ingrese un número válido (1, 2, 3 o 4).')
