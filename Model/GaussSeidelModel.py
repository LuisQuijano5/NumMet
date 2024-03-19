from tabulate import tabulate

def separar_matriz(matriz):
    n = len(matriz)
    matriz_cuadrada = []
    vector = []
    for fila in matriz:
        matriz_cuadrada.append(fila[:n])
        vector.append(fila[n])
    return matriz_cuadrada, vector

def gauss_seidel(matrizComp, ep):

    coeficientes,vectorCtes = separar_matriz(matrizComp)

    n = len(coeficientes)
    X = [0] * n

    iteramax=100
    heades = ['itera']

    errores=[]
    for i in range(n):
        errores.append(0)
        heades.append("x"+str(i+1))
        heades.append("xn"+str(i+1))
        heades.append("e"+str(i+1))

    error=ep*2
    itera=1

    sol=[]
    while(error>=ep and itera<=iteramax):
        row=[]
        row.append(itera)
        for i in range(n):
            suma = sum(coeficientes[i][j] * X[j] for j in range(n) if j != i)

            nuevo=round((vectorCtes[i]-suma)/coeficientes[i][i],6)

            errores[i]=round(abs(1-X[i]/nuevo)*100,6)

            row.append(X[i])
            row.append(nuevo)
            row.append(errores[i])

            X[i]=nuevo

        sol.append(row)
        error=max(errores)
        itera=itera+1


    if(itera>iteramax):
        X=0

    table=tabulate(sol,headers=heades,tablefmt='fancy_grid',floatfmt='.6f')

    return table,X
