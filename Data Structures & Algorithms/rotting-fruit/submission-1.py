from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        visited = set([(i, j) for i, j, _ in queue])

        while queue:
            i, j, dist = queue.popleft()
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols \
                        and grid[ni][nj] == 1 \
                        and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    fresh -= 1
                    minutes = max(minutes, dist + 1)
                    queue.append((ni, nj, dist + 1))

        return minutes if fresh == 0 else -1