# Administrador de Peticiones

# Importa las funciones y herramientas necesarias desde el módulo "herramientas"
from herramientas import separadorLineas, buscar, totalMovimientos, validacionInput

# Muestra un separador gráfico
separadorLineas("/")
# Muestra el título del programa
print(' ADMINISTRADOR DE PETICIONES')
# Muestra otro separador gráfico
separadorLineas("/")

# Solicita al usuario la cantidad de números que desea cargar
cantidad = int(input('¿Cuántos números desea cargar?: '))

# Inicializa una lista llamada "peticionInicial" para almacenar las posiciones a buscar
peticionInicial = []
# Solicita al usuario ingresar las posiciones a buscar y las agrega a la lista
for i in range(cantidad):
        nuevo_numero = int(input('Ingrese la siguiente posición a buscar en la memoria: '))
        peticionInicial.append(nuevo_numero)
        print('')  # Imprime una línea en blanco para mejorar la presentación

# Solicita al usuario la posición inicial desde donde desea comenzar la búsqueda
posicionInicial = int(input('¿En qué posición desea comenzar la búsqueda?: '))

# Muestra un separador gráfico
separadorLineas("/")
# Muestra un mensaje para que el usuario elija el método de búsqueda
print('Elija el método de búsqueda:')
# Muestra otro separador gráfico
separadorLineas("/")

# Llama a la función "validacionInput" para que el usuario seleccione un método de búsqueda
operacion = validacionInput()

# Muestra un separador gráfico
separadorLineas("/")

# Llama a la función "buscar" para realizar la búsqueda con el método seleccionado
ordenBusqueda = buscar(peticionInicial, operacion, posicionInicial)
# Llama a la función "totalMovimientos" para calcular el total de movimientos
movimientos = totalMovimientos(ordenBusqueda, posicionInicial)

# Muestra los resultados de la búsqueda
print(f'Lista en la entrada: {peticionInicial}')
print(f'Posición inicial: {posicionInicial}')
print(f'Resultado de la búsqueda: {ordenBusqueda}')
print(f'Total de movimientos: {movimientos}')
