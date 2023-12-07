def square_matrix_simple(matrix=[]):
    sqmatrix = []
    x=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x.append((matrix[i][j])**2)
        sqmatrix.append(x)
        x=[]

    return sqmatrix
