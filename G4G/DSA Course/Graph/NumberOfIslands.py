from typing import List

import sys

sys.setrecursionlimit(10**8)


class Solution:
    def numIslands(self, grid) -> int:
        cols: int = len(grid[0])
        rows: int = len(grid)
        visited: List[List[int]] = [[0] * cols for i in range(rows)]

        # Function to check if the given coordinates are valid or not.
        def isValid(row, col) -> bool:
            if (row >= 0 and row < rows) and (col >= 0 and col < cols):
                return True
            return False

        # Depth First Search to explore the connected components.
        def dfs(grid, row, col) -> None:
            visited[row][col] = 1
            for i in [
                [-1, -1],
                [1, 1],
                [1, 0],
                [0, 1],
                [1, -1],
                [-1, 1],
                [-1, 0],
                [0, -1],
            ]:
                if (
                    isValid(row=row + i[0], col=col + i[1])
                    and visited[row + i[0]][col + i[1]] == 0
                ):
                    if grid[row + i[0]][col + i[1]] == 1:
                        dfs(grid=grid, row=row + i[0], col=col + i[1])

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    dfs(grid=grid, row=i, col=j)
                    count += 1
        return count


def main() -> None:

    grid: List[List[int]] = [[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0]]
    for x in grid:
        for y in x:
            print(y, end="")
        print()
    print()
    s = Solution()
    print(f"Number of islands: {s.numIslands(grid=grid)}")


if __name__ == "__main__":
    main()
