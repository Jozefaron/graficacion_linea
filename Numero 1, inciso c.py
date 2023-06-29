    # Funcion que grafica una linea usando el algoritmo de Bresenham

# -----------     ENTRADA DE DATOS    -----------
# Esta funcion llamada Bresenham recibe como datos de entrada los valores (x1, y1, x2, y2)
# los cuales todos son introducidos por el usuario , tenemos que ("x1" y "x2")
#son las coordenadas donde inicia cada punto y ("y1" y "y2") donde termina...
#Se tendran que calcular  unas variables como ddy, ddx, p

# -----------     SALIDA DE DATOS    -----------
# Como salida tendremos las coordenada (X,Y)  junto con las operaciones realizadas en "p"
#tenemos que para el caso de que p<0 se incremente xi y se calcula p de una forma
# pero si p>0 incrementamos las dos variables y calculamos "p" de forma distinta y repetimos

# -----------    EJEMPLO    -----------
# X1 = 5, Y1 = 5 y X2 = 22 Y2 = 10
# dx = 17 y dy = 5  entonces tenemos ddy = 10, ddx = 34, p = -7, imprimimos
# p<0 si entonces incrementamos en uno Xi y calculamos p como p=-7+10, imprimimos
# evalua y entonces p>0 si entonces incrementamos Xi y Yi, calculamos p como p=3+10-34
#y asi sucesivamente
import time
from turtle import *
import timeit
tic = timeit.default_timer()
def Bresenham(Xi, Yi, Xf, Yf):
    print()
    print()
    print("Pk", "\t", "X", "\t", "Y")
    print("\t", Xi, "\t", Yi)
    dy = Yf - Yi
    dx = Xf - Xi
    ddy = 2 * dy
    ddx = 2 * dx
    p = ddy - dx
    setup(450, 500, 0, 0)
    screensize(400, 300)
    while Xi != Xf or Yi != Yf:
        if p < 0:
            Xi += 1
            print(p, "\t", Xi, "\t", Yi)
            goto(Xi, Yi)
            time.sleep(1)
            p = p + ddy
        elif p > 0:
            Yi += 1
            Xi += 1
            print(p, "\t", Xi, "\t", Yi)
            goto(Xi, Yi)
            time.sleep(1)
            p = p + ddy - ddx
    toc = timeit.default_timer()
    print(toc)
    toc - tic

Xi = int(input("Coordenada X inicial\t"))
Yi = int(input("Coordenada Y inicial\t"))
Xf = int(input("Coordenada X final\t"))
Yf = int(input("Coordenada Y final\t"))

Bresenham(Xi, Yi, Xf, Yf)