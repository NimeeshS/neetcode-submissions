from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        minutes = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (
                        0 <= i + di < len(grid) and
                        0 <= j + dj < len(grid[0]) and
                        grid[i + di][j + dj] == 1
                    ):
                        grid[i + di][j + dj] = 2
                        fresh -= 1
                        q.append((i + di, j + dj))

        return minutes if fresh == 0 else -1