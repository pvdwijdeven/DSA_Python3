import heapq


class Node:
    def __init__(self, data: int, row: int, col: int):
        self.data = data
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.data < other.data


def matrix_median(matrix):
    max_rows = len(matrix)
    max_columns = len(matrix[0])
    minheap = []
    count = 0
    median = -1
    medianindex = (max_rows * max_columns) // 2
    for row in range(max_rows):
        temp = Node(data=matrix[row][0], row=row, col=0)
        heapq.heappush(minheap, temp)
    while count <= medianindex:
        top = heapq.heappop(minheap)
        row = top.row
        col = top.col
        median = top.data
        count += 1
        if col + 1 < max_columns:
            col += 1
            temp = Node(data=matrix[row][col], row=row, col=col)
            heapq.heappush(minheap, temp)

    return median


if __name__ == "__main__":
    A = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    print(matrix_median(matrix=A))
