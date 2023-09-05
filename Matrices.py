A = [[12,8,4],[3, 17,14],[9,8,10]]
B = [[5,19,3],[6,15,9],[7,8,16]]
I = [[1,0,0],[0,1,0],[0,0,1]]
O = [[0,0,0],[0,0,0],[0,0,0]]

def printMatrix(M):
    for i in M:
        print(i)

def transpose(M):
    O = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,len(M)):
        for j in range(0,len(M)):
            O[i][j] = M[j][i]
    return O

def det3x3(M):
    det = (M[0][0] * ((M[1][1] * M[2][2]) - (M[2][1] * M[1][2]))) - (M[0][1] * ((M[1][0] * M[2][2]) - (M[2][0] * M[1][2]))) + (M[0][2] * ((M[1][0] * M[2][1]) - (M[2][0] * M[1][1])))
    return det

def det2x2(M):
    det = M[0][0] * M[1][1] - M[1][0] * M[0][1]
    return det

def scalerMx(S,M):
    for i in range(0,len(M)):
        for j in range(0,len(M)):
            M[i][j] = S*M[i][j]
    return M

def minorMatrix3x3(M):
    X = [[0,0,0],[0,0,0],[0,0,0]]
    X[0][0] = det2x2([[M[1][1], M[1][2]] , [M[2][1], M[2][2]]])
    X[0][1] = det2x2([[M[1][0], M[1][2]] , [M[2][0], M[2][2]]])
    X[0][2] = det2x2([[M[1][0], M[1][1]] , [M[2][0], M[2][1]]])

    X[1][0] = det2x2([[M[0][1], M[0][2]] , [M[2][1], M[2][2]]])
    X[1][1] = det2x2([[M[0][0], M[0][2]] , [M[2][0], M[2][2]]])
    X[1][2] = det2x2([[M[0][0], M[0][1]] , [M[2][0], M[2][1]]])

    X[2][0] = det2x2([[M[0][1], M[0][2]] , [M[1][1], M[1][2]]])
    X[2][1] = det2x2([[M[0][0], M[0][2]] , [M[1][0], M[1][2]]])
    X[2][2] = det2x2([[M[0][0], M[0][1]] , [M[1][0], M[1][1]]])

    return X

def cofactorMatrix3x3(M):

    X = [[0,0,0],[0,0,0],[0,0,0]]
    X[0][0] = det2x2([[M[1][1], M[1][2]] , [M[2][1], M[2][2]]])
    X[0][1] = -1*det2x2([[M[1][0], M[1][2]] , [M[2][0], M[2][2]]])
    X[0][2] = det2x2([[M[1][0], M[1][1]] , [M[2][0], M[2][1]]])

    X[1][0] = -1*det2x2([[M[0][1], M[0][2]] , [M[2][1], M[2][2]]])
    X[1][1] = det2x2([[M[0][0], M[0][2]] , [M[2][0], M[2][2]]])
    X[1][2] = -1*det2x2([[M[0][0], M[0][1]] , [M[2][0], M[2][1]]])

    X[2][0] = det2x2([[M[0][1], M[0][2]] , [M[1][1], M[1][2]]])
    X[2][1] = -1*det2x2([[M[0][0], M[0][2]] , [M[1][0], M[1][2]]])
    X[2][2] = det2x2([[M[0][0], M[0][1]] , [M[1][0], M[1][1]]])

    return X

def inverse3x3(M):
    M = cofactorMatrix3x3(M)
    M = transpose(M)
    M = scalerMx(1/det3x3(M), M)
    return M

def matrixMultiplication(A,B):
    X = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                X[i][j] += A[i][k] * B[k][j]

    return X

def matrixAdd(A,B):
    X = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            X[i][j] = A[i][j] + B[i][j]
    return X

def matrixSubtract(A,B):
    X = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            X[i][j] = A[i][j] - B[i][j]
    return X
