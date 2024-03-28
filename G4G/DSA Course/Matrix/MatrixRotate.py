def rotate_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(row + 1, cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    for row in range(rows // 2):
        matrix[row], matrix[rows - row - 1] = matrix[rows - row - 1], matrix[row]

    return matrix


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(rotate_matrix(matrix=A))
    B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(matrix=B))
