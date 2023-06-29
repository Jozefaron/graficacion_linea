# Funcion que grafica una linea con pendiente m>1 y con m<0

# -----------     ENTRADA DE DATOS    -----------
# Esta funcion llamada grafica recibe como datos de entrada los valores (Xi, Yi, Xf Yf)
# los cuales todos son introducidos por el usuario , tenemos que ("Xi" y "Xi)
#son las coordenadas donde inicia cada punto y ("Yf" y "Yf") donde termina...
#notamos que tenemos dos funciones ya que para pendiente menor a 0 o manor se llama
#a cierta funcion y se realizan pasos muy similares

# -----------     SALIDA DE DATOS    -----------
# Como salida tendremos las coordenada (X,Y) donde se incrementara el valor de "x" o "y",
# usamos el algoritmo de bresenham solo que para estoen el caso de m>1 se deberan intercambiar
#los puntos al igual que para el caso m<0 y procederemos a calcular

# -----------    EJEMPLO    -----------
# Xi = 1, Yi = 2 y Xf = 5, Yf = 10
#calculamos una pendiente que para este caso es positiva y llamamos a Bresenham()
# intercambiamos los valores como se indica en Cambio de variables 1.0
# dx = 9 y dy = 3 entonces calculamos p = -3
#  entonces entramos a p<0 y realizamos lo siguiente
# se incrementa Xi en uno, imprimimos, graficamos, y calculamos p, asi sucesivamente

from turtle import *
import time
import timeit
tic = timeit.default_timer()

def BresenhamP(Xi, Yi, Xf, Yf):
#cambio de variables 1.0
    aux = Yi
    Yi = Xi
    Xi = aux
    aux2 = Yf
    Yf = Xf
    Xf = aux2
    print()
    print("Pendiente positiva")
    print("Xi=", Xi, "\t", "Yi=", Yi, "\t", "Xf=", Xf, "\t", "Yf=", Yf)
    dy = Xf - Yi
    dx = Yf - Xi
    ddy = 2 * dy
    ddx = 2 * dx
    p = ddy - dx
    print("dy=", dy, "\t", "dx=", dx, "\t", "ddy=", ddy, "\t", "ddx=", ddx, "\t", "p=", p)
    print()
    print("P", "\t", "X", "\t", "Y")
    print("\t", Xi, "\t", Yi)
    setup(450, 500, 0, 0)
    title("Pendiente positiva")
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
    time.sleep(10)

def BresenhamN(Xi, Yi, Xf, Yf):
#cambio de variables 1.0
    aux = Yi
    Yi = Xi
    Xi = Yf
    Yf = aux
    print()
    print("Pendiente negativa")
    print("Xi=", Xi, "\t", "Yi=", Yi, "\t", "Xf=", Xf, "\t", "Yf=", Yf)
    dy = Xf - Yi
    dx = Yf - Xi
    ddy = 2 * dy
    ddx = 2 * dx
    p = ddy - dx
    print("dy=", dy, "\t", "dx=", dx, "\t", "ddy=", ddy, "\t", "ddx=", ddx, "\t", "p=", p)
    print()
    print("P", "\t", "X", "\t", "Y")
    print("\t", Xi, "\t", Yi)
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
m = (Xf - Xi) - (Yi - Yf)

if m > 1:
    ## Para pendiente positiva
    BresenhamP(Xi, Yi, Xf, Yf)
elif m < 0:
    ##Para pendiente negativa
    BresenhamN(Xi, Yi, Xf, Yf)