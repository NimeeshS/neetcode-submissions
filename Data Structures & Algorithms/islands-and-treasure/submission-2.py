class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(i, j, dist):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return
            if grid[i][j] == -1:
                return
            if grid[i][j] < dist:
                return
            grid[i][j] = dist
            dfs(i + 1, j, dist + 1)
            dfs(i - 1, j, dist + 1)
            dfs(i, j + 1, dist + 1)
            dfs(i, j - 1, dist + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: dfs(i, j, 0)