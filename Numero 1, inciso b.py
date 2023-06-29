# Funcion que grafica una linea dados usando algoritmo DDA (Digital Differential Analizer)

# -----------     ENTRADA DE DATOS    -----------
# Esta funcion llamada grafica recibe como datos de entrada los valores (x1, y1, x2, y2)
# los cuales todos son introducidos por el usuario , tenemos que ("x1" y "x2")
#son las coordenadas donde inicia cada punto y ("y1" y "y2") donde termina...
# Asi mismo  calculamos dy, dx, y m

# -----------     SALIDA DE DATOS    -----------
#depedera de dos casos cuando m<1 entonces  x1 incrementara 1 y y1 sera igual a y1 mas m
#se repetira  hasta que X1 sea igual a X2 (Xinicial == Xfinal)
#por otro caso tenemos que m>1 entonces y1 se incrementara en 1 y calculamos a x1 como
#x1 igual a x1 mas (1/m) y lo imprimimos asi sucesivamente

# -----------    EJEMPLO    -----------
# X1 = 5, Y1 = 2 y X2 = 8, Y2 = 21
# dx = 3 y dy = 19 entonces m = 6.33
# entonces m>1 se imprime y1, floor(5+.5), 5.00
# se incrementa Y1 y se calcula X1 como X1 mas 1/m

from turtle import *
import math
import time
import timeit
tic = timeit.default_timer()

def DDA(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    m = dy / dx
    print()
    print("dy=", dy, "\t", "dx=", dx, "\t", "m=", "%.2f" % m)
    if m < 1:
        print()
        print("X\t Y\t P")
    elif m > 1:
        print()
        print("Y\t X\t P")
    setup(450, 500, 0, 0)
    screensize(400, 300)
        #pendiente menor < 1
    if m < 1:
        while x1 != x2:
            x1 += 1
            y1 += m
            print(x1, "\t", math.floor(y1 + .5), "\t", "%.2f" % y1)
            goto(x1, y1)
            colormode(255)
            time.sleep(1)
            #pendiente mayor > 1
    else:
        while y1 != y2:
            print(y1, "\t", math.floor(x1 + .5), "\t", "%.2f" % x1)
            goto(x1, y1)
            colormode(255)
            time.sleep(1)
            y1 += 1
            x1 += (1 / m)
    toc = timeit.default_timer()
    print(toc)
    toc - tic
    time.sleep(10)
x1 = int(input("Coordenada X1\t"))
y1 = int(input("Coordenada Y1\t"))
x2 = int(input("Coordenada X2\t"))
y2 = int(input("Coordenada Y2\t"))

DDA(x1, y1, x2, y2)