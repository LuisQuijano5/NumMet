import numpy as np

def diferencias(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    print(coef)

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    print(coef)
    return coef[0, :]


def interpolacion(coef, valores_x, buscado):
    n = len(coef) - 1
    suma = coef[n]

    for k in range(1, n + 1):
        suma = coef[n - k] + (buscado - valores_x[n - k]) * suma

    suma=round(suma,6)

    return suma

def calcularPunto(x,y,x_eval):
    coeficientes = diferencias(x, y)

    y_eval = interpolacion(coeficientes, x, x_eval)

    print("Coeficientes de las diferencias divididas:", coeficientes)
    print(f"Valor interpolado en x = {x_eval}: y = {y_eval}")
    return y_eval



