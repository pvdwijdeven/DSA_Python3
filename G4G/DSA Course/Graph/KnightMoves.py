class Solution:

    # Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        from collections import deque

        source_row = KnightPos[0] - 1
        source_col = KnightPos[1] - 1
        destination = (TargetPos[0] - 1, TargetPos[1] - 1)
        queue = deque([(source_row, source_col, 0)])
        moves = [
            (2, 1),
            (1, 2),
            (-2, 1),
            (-1, 2),
            (2, -1),
            (1, -2),
            (-2, -1),
            (-1, -2),
        ]

        visited = set()
        while queue:
            row, col, step = queue.popleft()
            if (row, col) == destination:
                return step
            for move_row, move_col in moves:
                row_delta = move_row + row
                col_delta = move_col + col
                row_inbound = 0 <= row_delta < N
                col_inbound = 0 <= col_delta < N
                if not row_inbound or not col_inbound:
                    continue
                if (row_delta, col_delta) not in visited:
                    queue.append((row_delta, col_delta, step + 1))
                    visited.add((row_delta, col_delta))
        return -1
