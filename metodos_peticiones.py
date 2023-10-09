# Implementación del algoritmo SSTF (Shortest Seek Time First)
def SSTF(lista, actual):
    ordenSalida = []  # Lista que contendrá el orden de búsqueda

    while lista:
        menorDistancia = float('inf')  # Inicializar la menor distancia como infinito
        siguiente = None

        # Buscar el número más cercano al actual
        for numero in lista:
            distancia = abs(numero - actual)  # Calcular la distancia
            if distancia < menorDistancia:
                menorDistancia = distancia
                siguiente = numero
        
        actual = siguiente  # Actualizar la posición actual
        ordenSalida.append(siguiente)  # Agregar el número al orden de búsqueda
        lista.remove(siguiente)  # Eliminar el número de la lista original

    return ordenSalida  # Devolver el orden de búsqueda

# Implementación del algoritmo Scan por mayores primero
def scanA(lista, actual):
    ordenSalida = []  # Lista que contendrá el orden de búsqueda

    mayores = [numero for numero in lista if numero > actual]  # Sectores mayores al actual
    menores = [numero for numero in lista if numero <= actual]  # Sectores menores o iguales al actual

    # Ordenar las listas para el escaneo
    mayores.sort()
    menores.sort(reverse=True)

    ordenSalida.extend(menores)  # Agregar los menores primero
    ordenSalida.extend(mayores)  # Luego los mayores

    return ordenSalida  # Devolver el orden de búsqueda

# Implementación del algoritmo Scan por menores primero
def scanB(lista, actual):
    ordenSalida = []  # Lista que contendrá el orden de búsqueda

    menores = [numero for numero in lista if numero < actual]  # Sectores menores al actual
    mayores = [numero for numero in lista if numero >= actual]  # Sectores mayores o iguales al actual

    # Ordenar las listas para el escaneo
    menores.sort(reverse=True)
    mayores.sort()

    ordenSalida.extend(menores)  # Agregar los menores primero
    ordenSalida.extend(mayores)  # Luego los mayores

    return ordenSalida  # Devolver el orden de búsqueda

# Implementación del algoritmo Scan Circular
def scanCircular(lista, actual):
    primeraVuelta = [numero for numero in lista if numero >= actual]  # Sectores en la primera vuelta
    segundaVuelta = [numero for numero in lista if numero < actual]  # Sectores en la segunda vuelta

    # Ordenar ambas listas y combinarlas
    ordenSalida = sorted(primeraVuelta) + sorted(segundaVuelta)

    return ordenSalida  # Devolver el orden de búsqueda


