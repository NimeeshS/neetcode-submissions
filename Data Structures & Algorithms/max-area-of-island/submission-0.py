class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return 0
            if (i, j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return 1 + dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)

        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                m = max(m, dfs(i, j))

        return m