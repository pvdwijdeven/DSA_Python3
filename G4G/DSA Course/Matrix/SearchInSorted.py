# search element in row- and column-wise sorted matrix
def search_in_sorted(matrix, x):
    max_rows = len(matrix)
    max_cols = len(matrix[0])
    row = 0
    col = max_cols - 1
    while row < max_rows and col >= 0:
        if matrix[row][col] == x:
            return [row, col]
        if matrix[row][col] > x:
            col -= 1
        else:
            row += 1
    return []


if __name__ == "__main__":
    A = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    print(search_in_sorted(matrix=A, x=29))
