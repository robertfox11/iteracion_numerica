import sympy as sp
# from sympy import *
import math

a = 0
b = 1
n = 6


def integraDefProfe(x):
    """Ejemplo de regla Simpsom  ejercicio"""
    y = 1 + math.exp(-x) * math.sin(4 * x)
    # y = x * math.exp(x)
    return round(y, 4)


def limofIntegralH(b, a, n):
    """Espaciado de la ingegral """
    pn = n - 1
    h = (b - a) / pn
    return round(h, 4)


h = limofIntegralH(b, a, n)
def arraytramoFx():
    """Tramos entre a y b de la integral definida"""
    cnt = 0
    arrayTramos = []
    if b < a:
        print("No se puede realizar la integral de la regla de simpson")
        return 1

    tramo = int(b / h)
    tramo2 = int(abs(a) / h)
    tramo = tramo + tramo2
    print(tramo)
    hi = a
    while cnt <= tramo:
        hin = round(h + hi, 3)
        arrayTramos.append(hin)
        hi += h
        cnt += 1

    # tramo = tramo - 1
    arraySumTramos = arrayTramos[0:tramo]
    return arraySumTramos


arrayTramofx = arraytramoFx()

def reglaSimpsonCompuesta(h, arraSumtramosToFx, a):
    """regla de trapecio compuesta, """
    h2 = h / 6
    arrayFxP = []
    fxaux = 0
    for i, fxp in enumerate(arraSumtramosToFx):
        """Aproximacion a la integral"""
        if i > 0:
            sumFxt = round(fxp + fxaux, 2)
            arrayFxP.append(integraDefProfe(fxp) + integraDefProfe(fxaux) + 4 * integraDefProfe(sumFxt / 2))
            fxaux = fxp
        else:
            fxaux = fxp
            arrayFxP.append(integraDefProfe(fxp) + 4 * integraDefProfe((fxp + a) / 2) + integraDefProfe(a))

    integralAproxFx = round(sum(arrayFxP) * h2, 5)
    return integralAproxFx


print(reglaSimpsonCompuesta(h, arrayTramofx, a))


