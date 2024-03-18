def separar_matriz(matriz):
    n = len(matriz)
    matriz_cuadrada = []
    vector = []
    for fila in matriz:
        matriz_cuadrada.append(fila[:n])
        vector.append(fila[n])
    return matriz_cuadrada, vector


#matrixComp = [[6, -1, -1, 4, 17],
#              [1, -10, 2, -1, -17],
#              [3, -2, 8, -1, 19],
#              [1, 1, 1, -5, -14]]

def gauss_seidel(matrizComp, ep):

    coeficientes,vectorCtes = separar_matriz(matrizComp)

    n = len(coeficientes)
    X = [0] * n

    iteramax=100
    historial = "itera | "

    errores=[]
    for i in range(n):
        errores.append(0)
        historial=historial+"x"+str(i)+" | xn"+str(i)+" | e"+str(i)+" | "

    historial=historial+"\n"
    error=ep*2
    itera=1


    while(error>=ep and itera<=iteramax):
        historial=historial+str(itera)+" | "
        for i in range(n):
            suma = sum(coeficientes[i][j] * X[j] for j in range(n) if j != i)

            nuevo=round((vectorCtes[i]-suma)/coeficientes[i][i],6)

            errores[i]=round(abs(1-X[i]/nuevo)*100,6)

            historial=historial + str(X[i])+" | "+str(nuevo)+" | "+str(errores[i])+" | "

            X[i]=nuevo
        error=max(errores)
        itera=itera+1
        historial=historial+"\n"

    if(itera>iteramax):
        X=0

    return historial,X
