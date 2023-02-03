import sympy as sp
# from sympy import *
import math


def integraDef(parI):
    """Ejemplo de trapecio simple ejercicio"""
    x = sp.Symbol('x')
    y = sp.exp(-parI ** 2)
    # print(y)
    res = sp.integrate(y, (x, 1, 2))
    return round(res.evalf(), 4)


def integraDef2(parI):
    """Ejemplo de trapecio simple ejercicio de viu"""
    x = sp.Symbol('x')
    y = 1 + sp.exp(-parI) * math.sin(4 * parI)
    res = sp.integrate(y, (x, 0, 1))
    return round(res.evalf(), 4)


# print(integraDef2(2))
"""Regla Trapecio Compuesta"""
"""a es el valor minimo de la integral definida y b es
el valor maximo, n es el numero iteraciones que da a la funcino para la regla de trapecio
 compuesta"""
a = -6
b = -3
n = 20


def integralFunEjerCompuesta():
    """Ejercico con la interal definidida
     se puede cambiar con culquier funcino para comprobar el resultag
    3x^2"""
    x = sp.Symbol('x')
    y = 3 * x ** 2
    res = sp.integrate(y, (x, a, b))
    return round(res.evalf(), 4)


print(integralFunEjerCompuesta())


def integralFunEjerCompuestaPar(pari):
    """Integral definida recibiendo un parametro para recorrer
    los tramos que esta entre la integral definidad de a  y b"""
    y = round(3 * pari ** 2, 4)

    return y


def limofIntegralH(b, a, n):
    pn = n - 1
    h = (b - a) / pn
    return round(h, 1)


h = limofIntegralH(b, a, n)
print(h)
"""tramos de a hacia b donde es a = 0 y b= 2 y el tramo es h
    y h = 0.4 
"""


def reglaTrapecioCompuesta(h, arraSumtramosToFx, a, b):
    """regla de trapecio compuesta
    Reibe como parametro h, es el espacio que hay entre el valaor minimo de a y b
    entre 2, segundo parametro recibe un array de tramos con espaciado de a y b ,
    tercer paraemtro a es el valor minimo del al integal y b el valor maximo de la
    integral definida"""
    h2 = h / 2
    arrayFx = []
    for tfx in arraSumtramosToFx:
        arrayFx.append(integralFunEjerCompuestaPar(tfx))

    integralCompuesta = round(
        h2 * (integralFunEjerCompuestaPar(a) + (sum(arrayFx) * 2) + integralFunEjerCompuestaPar(b)), 4)
    return integralCompuesta


# arrayTramos.append(h)

# h = round(h + h, 2)

def arraytramoFx():
    """Array que obtiene los tramos de a y b de la integral"""
    cnt = 0
    arrayTramos = []
    tramo = int(b / h)
    tramo2 = int((abs(a) / h))
    tramo = tramo + tramo2
    hi = a
    while cnt <= tramo:
        hin = round(h + hi, 2)
        arrayTramos.append(hin)
        hi += h
        cnt += 1

    tramo = tramo - 1
    arraySumTramos = arrayTramos[0:tramo]
    return arraySumTramos


arraySumTramos = arraytramoFx()

print(reglaTrapecioCompuesta(h, arraySumTramos, a, b))


def reglaTrapecioCompuesta2():
    """Funcion que se puede realizar llamado la regla de trapecion compuesta """
    arraySumTramos = arraytramoFx()
    return reglaTrapecioCompuesta(h, arraySumTramos, a, b)


print(reglaTrapecioCompuesta2())
#

#
# arrayParticiones= []
# lenParticiones = len(arrayParticiones) - 1
# arrayreglatrapecio = []
# cnt = 0
# while cnt < lenParticiones:
#     for idx, ts in enumerate(arrayParticiones):
#         if idx == 0:
#             x0 = ts
#             fx0 = round(integraDef2(ts), 4)
#             continue
#         if idx == 1:
#             x1 = ts
#             fx1 = integraDef2(ts)
#             print(fx1, ' + ', fx0)
#             print(x1, ' + ', x0)
#             # arrayreglatrapecio.append(round(reglaTrapecioSimple(fx1, fx0, x1, x0), 5))
#             # arrayParticiones.pop(0)
#     cnt += 1


# arrayParticiones = [0, 1, 1.6, 2]
# arrayParticiones = [0, 1]
# # print(arrayParticiones[1+1])
# lenParticiones = len(arrayParticiones) - 1
# print(lenParticiones)
"""Trapecio Simple"""


def reglaTrapecioSimple(fx1, fx0, x1, x0):
    res = ((fx1 + fx0) * (x1 - x0)) / 2
    return res

#
# def contadorParticiones():
#     arrayreglatrapecio = []
#     cnt = 0
#     while cnt < lenParticiones:
#         for idx, ts in enumerate(arrayParticiones):
#             if idx == 0:
#                 x0 = ts
#                 fx0 = round(integraDef2(ts), 4)
#                 continue
#             if idx == 1:
#                 x1 = ts
#                 fx1 = integraDef2(ts)
#                 print(fx1, ' + ', fx0)
#                 print(x1, ' + ', x0)
#                 arrayreglatrapecio.append(round(reglaTrapecioSimple(fx1, fx0, x1, x0), 5))
#                 arrayParticiones.pop(0)
#         cnt += 1
#     return arrayreglatrapecio


# res = contadorParticiones()
# print(res)
# print(print("regla de trapecio simple "), sum(res))
# pi = sp.pi**2
# print(pi.evalf())
