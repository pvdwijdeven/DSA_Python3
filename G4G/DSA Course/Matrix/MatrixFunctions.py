def print_matrix(matrix):
    max_rows = len(matrix)
    max_cols = len(matrix[0])
    print(f"Matrix {max_rows}x{max_cols}:")
    max_len = 0
    for row in range(max_rows):
        for col in range(max_cols):
            cur_len = len(str(matrix[row][col]))
            max_len = max(cur_len, max_len)
    for row in range(max_rows):
        if 0 < row:
            print()
        for col in range(max_cols):
            cur_val = str(matrix[row][col]).rjust(max_len)
            if col > 0:
                cur_val = " " + cur_val
            print(cur_val, end="")
    print()


# Function to add two matrices.
def sum_matrix(matrix_A, matrix_B):
    max_rows = len(matrix_A)
    max_cols = len(matrix_A[0])
    if max_rows != len(matrix_B) or max_cols != len(matrix_B[0]):
        return []
    C = [[0 for col in range(max_cols)] for row in range(max_rows)]
    for row in range(max_rows):
        for col in range(max_cols):
            C[row][col] = matrix_A[row][col] + matrix_B[row][col]
    return C


def sum_triangles(matrix):
    n = len(matrix)
    upper = 0
    lower = 0
    for row in range(n):
        for col in range(row, n):
            if row == col:
                upper += matrix[row][col]
                lower += matrix[row][col]
            else:
                upper += matrix[row][col]
                lower += matrix[col][row]
    return [upper, lower]


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
                res[row_A][col_B] += matrix_A[row_A][rowcol] * matrix_B[rowcol][col_B]
    return res


class Solution:
    a = 0


if __name__ == "__main__":
    s = Solution()
    A = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
    B = [[11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 0]]
    C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = sum_matrix(matrix_A=A, matrix_B=B)
    print_matrix(matrix=res)
    res = sum_matrix(matrix_A=A, matrix_B=A)
    print_matrix(matrix=res)
    print(sum_triangles(matrix=C))
    A = [[4, 8], [0, 2], [1, 6]]
    B = [[5, 2], [9, 4]]
    res = multiply_matrix(A, B)
    print_matrix(res)
