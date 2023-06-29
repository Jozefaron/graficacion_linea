# Funcion que grafica una linea dados dos puntos

# -----------     ENTRADA DE DATOS    -----------
# Esta funcion llamada grafica recibe como datos de entrada los valores (x1, y1, x2, y2)
# los cuales todos son introducidos por el usuario , tenemos que ("x1" y "x2")
#son las coordenadas donde inicia cada punto y ("y1" y "y2") donde termina...

# -----------     SALIDA DE DATOS    -----------
# Como salida tendremos las coordenada (X,Y) donde se incrementara el valor de "x" o "y",
# notamos que tambien se usa el metodo floor de la libreria math que  nos ayudara a
#redondear si un valor es que tiene en la parte flotante  mayor a .5 o menor a .5

# -----------    EJEMPLO    -----------
# X1 = 2, Y1 = 5 y X2 = 10, Y2 = 6
# dx = 8 y dy = 1 entonces m = 0.125
# imprimir X1, floor(5+.5), 5 = 5
# se incrementa X1 y se calcula Y1

import math
import time
from turtle import *
import timeit
tic = timeit.default_timer()

def grafica(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
    b = y2 - m * x2
    print()
    if m < 0:
        print("K\tX\tY")
    else:
        print("K\tX\tY")
        setup(400, 500, 0, 0)
        screensize(400, 300)
    while x1 != x2:
#caso 1
        if m < 1:
            while x1 != x2:

                print(x1, "\t", math.floor(y1 + .5), "\t", "%.2f" % y1)
                x1 = x1 + 1
                y1 = ((m * x1) + b)
                goto(x1, y1)
                time.sleep(1)
        else:
            while y1 != y2:

                print("%.2f\t" % x1, math.floor(x1 + .5), "\t", y1)
                y1 = y1 + 1
                x1 = ((y1 - b) / m)
                goto(x1, y1)
                time.sleep(1)
    toc = timeit.default_timer()
    print(toc)
    toc - tic
    time.sleep(10)
x1 = int(input("Coordenada X1\t"))
y1 = int(input("Coordenada Y1\t"))
x2 = int(input("Coordenada X2\t"))
y2 = int(input("Coordenada Y2\t"))

grafica(x1, y1, x2, y2)