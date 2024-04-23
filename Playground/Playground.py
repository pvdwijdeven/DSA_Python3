def multiply_matrix(matrix_A, matrix_B):
    rows_A = len(matrix_A)
    cols_A = len(matrix_A[0])
    rows_B = len(matrix_B)
    cols_B = len(matrix_B[0])
    if cols_A != rows_B:
        return []
    res = [[0 for col in range(cols_B)] for row in range(rows_A)]
    for row_A in range(rows_A):
        for col_B in range(cols_B):
            for rowcol in range(rows_B):
                res[row_A][col_B] += (
                    matrix_A[row_A][rowcol] * matrix_B[rowcol][col_B]
                ) % 1000000007
    return res


A = [[1, 1], [1, 0]]
n = 45
res = A.copy()
for n in range(n - 1):
    res = multiply_matrix(res, A)
print(res[1][0] % 1000000007)
