def gauss_jordan(A):
    # Number of eq and data structure to save states
    n = len(A)
    state = []

    # Perform elimination
    for i in range(n):

        # Check if the element in the main diagonal is 0
        if A[i][i] == 0:
            # Find a row below with a non-zero element in the same column
            found = False
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    # Exchange rows i and j
                    A[i], A[j] = A[j], A[i]
                    found = True
                    break  # Exit the loop once the exchange is done
            if not found:
                raise ValueError("Matrix is singular")

        #divide current row by the diagonal element to make it 1
        divisor = A[i][i] # 0,0 -> 1,1 ...
        for j in range(i, n + 1):
            A[i][j] /= divisor
        state.append([row[:] for row in A])
        # Make all other elements in the current colun zero, n cuz its te amount of eq
        for k in range(n):
            if k != i: # To avoid making the current eq and var zero
                multiplier = A[k][i]
                for j in range(i, n + 1): # goes through the eq
                    A[k][j] -= multiplier * A[i][j]
        # Save the state after this iteration
        state.append([row[:] for row in A])
    # extratc solution vector
    x = [row[n] for row in A]
    return x, state[1:]



#A = [[2, 1, 5], [4, 4, 6]]

#A = [[1, 1, 2], [3, -5, -2]]
#solution, state = gauss_jordan(A) #tuple
#print("Solution:", solution)
#print("State after each iteration:")
#for i, matrix in enumerate(state):
#    print(f"Iteration {i+1}:")
#    for row in matrix:
#        print(row)