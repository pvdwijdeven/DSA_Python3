def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(row + 1, cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix


if __name__ == "__main__":
    A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print(transpose_matrix(matrix=A))
