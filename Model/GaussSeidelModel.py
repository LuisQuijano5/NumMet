from tabulate import tabulate

def separar_matriz(matriz):
    n = len(matriz)
    matriz_cuadrada = []
    vector = []
    for fila in matriz:
        matriz_cuadrada.append(fila[:n])
        vector.append(fila[n])
    return matriz_cuadrada, vector

def check_matrix(matrix, n):
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    return matrix
            return False
    return matrix


def gauss_seidel(matrizComp, ep):
    aux = check_matrix(matrizComp, len(matrizComp))
    if not aux:
        aux = check_matrix(list(reversed(matrizComp)), len(matrizComp))
        if not aux:
            raise ValueError("Matrix is singular")
    matrizComp = aux

    coeficientes,vectorCtes = separar_matriz(matrizComp)

    n = len(coeficientes)
    X = [0] * n

    iteramax=100
    heades = ['itera']

    errores=[]
    for i in range(n):
        errores.append(0)
        heades.append(f"x{i+1}")
        heades.append(f"xn{i+1}")
        heades.append(f"e{i+1}")

    error=ep*2
    itera=1

    sol=[]
    while(error>=ep and itera<=iteramax):
        row=[]
        row.append(itera)
        for i in range(n):
            suma = sum(coeficientes[i][j] * X[j] for j in range(n) if j != i)

            nuevo=round((vectorCtes[i]-suma)/coeficientes[i][i], 6)

            tolerance = 1e-6
            if abs(nuevo) > tolerance:
                errores[i] = round(abs(1 - X[i] / nuevo) * 100, 6)
            else:
                errores[i] = 100

            row.append(X[i])
            row.append(nuevo)
            row.append(errores[i])

            X[i]=nuevo

        sol.append(row)
        error=max(errores)
        itera=itera+1


    if(itera>iteramax):
        X=0

    table=tabulate(sol,headers=heades,tablefmt='plain',numalign='decimal',floatfmt='.6f')

    return table,X


#matriz = [[10, 2, 1, 7], [1, 5, 1, -8], [2, 3, 10, 6]]
#matriz = [[4, -1, 2, 3], [1, 6, -1, 12], [-2, 1, 5, -2]]
#matriz = [[1,2,4], [1,0,5]]
#matriz = [[6, -1, -1, 4, 17],
#          [1, -10, 2, -1, -7],
#          [3, -2, 8, -1, 19],
#          [1, 1, 1, -5, -14]]
#ep = 1e-6
#result_table, solution = gauss_seidel(matriz, ep)
#print(result_table)
#print("Solution:", solution)

