# Administrador de Peticiones

## GENERAL:

Este es un proyecto en Python que simula la administración de peticiones para recuperar bloques (sectores) de un archivo en una unidad de almacenamiento secundaria.

## Descripción del Proyecto

El objetivo de este proyecto es implementar algoritmos de administración de peticiones que permitan recuperar sectores de un archivo de manera eficiente. Se han implementado cuatro métodos de administración:

1. FCFS (First Come, First Served): Servicio por orden de llegada, similar a FIFO (First In, First Out). Los sectores se recuperan en el orden en que se solicitaron.

2. SSTF (Shortest Seek Time First): Elige el sector más cercano a la posición actual de la cabeza lectora en cada paso, minimizando el tiempo de búsqueda.

3. SCAN: Algoritmo de elevador que busca en una dirección hasta alcanzar el extremo y luego invierte la dirección. Selecciona sectores en el camino según su proximidad a la posición actual.

4. C-SCAN (Circular Scan): Variante del algoritmo SCAN que opera de manera circular. Desplaza la cabeza lectora en una dirección hasta alcanzar el extremo y luego regresa al inicio sin buscar en la dirección opuesta.

## Supuestos y Restricciones

- El archivo a recuperar es único y consta de una cantidad variable de sectores (de 1 a n).
- Los sectores están numerados de 1 a 1000 y su distribución es ordenada de menor a mayor, siguiendo el modelo de Logical Block Addressing (LBA).
- La lista de sectores que componen el archivo se proporciona completa.
- Se proporciona el último sector leído.
- No se permite alterar la lista de sectores en ningún método de administración.

## Uso del Proyecto

Para utilizar este proyecto, sigue estos pasos:

Descarga o clona el repositorio.
$ git clone https://github.com/emadiaz15/Administrador_peticiones.git

Ejecuta el programa principal:
$ python main.py

## Tecnologías utilizadas

* Python

## Autor ✒️

**Emanuel Diaz**  - [emadiaz15](https://github.com/emadiaz15)
