import random


def swap(matrix, ai, aj, bi, bj):
    matrix[ai][aj], matrix[bi][bj] = matrix[bi][bj], matrix[ai][aj]


def matrixGenerator(m, n, min_limit=0, max_limit=9):
    a = [[random.randint(min_limit, max_limit) for i in range(n)] for j in range(m)]
    for i in range(m):
        print(a[i])
    return a


def diagonalSort(matrix, m, n):
    for str in range(m-2, -1, -1):
        for i in range(0, min(m-str-1, n-1), +1):
            for j in range(0, min(m-str-1, n-1), +1):
                if matrix[j+str][j] > matrix[j+str+1][j+1]:
                    # print(matrix[j+str][j], matrix[j+str+1][j+1])
                    swap(matrix, j+str, j, j+str+1, j+1)
                    # print(matrix)

    for col in range(1, n-1, +1):
        for i in range(0, min(n-col-1, m-1), +1):
            for j in range(0, min(n-col-1, m-1), +1):
                if matrix[j][j+col] > matrix[j+1][j+col+1]:
                    # print(matrix[j][j+col], matrix[j+1][j+col+1])
                    swap(matrix, j, j+col, j+1, j+col+1)
                    # for k in range(5):
                    #     print(a[k])
    return matrix


# a = matrixGenerator(8, 6, 0, 9)
# a = diagonalSort(a, 8, 6)
# print('')
# for i in range(8):
#     print(a[i])