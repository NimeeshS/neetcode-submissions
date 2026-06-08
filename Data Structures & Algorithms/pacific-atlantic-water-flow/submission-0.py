class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def checkPacific(i, j, h, visited):
            if (i, j) in visited:
                return False
            if (i < 0 or j < 0):
                return True
            if not (0 <= i < len(heights) and 0 <= j < len(heights[0])):
                return False
            if heights[i][j] > h:
                return False
            visited.add((i, j))
            return (
                checkPacific(i + 1, j, heights[i][j], visited) or
                checkPacific(i - 1, j, heights[i][j], visited) or
                checkPacific(i, j + 1, heights[i][j], visited) or
                checkPacific(i, j - 1, heights[i][j], visited)
            )

        def checkAtlantic(i, j, h, visited):
            if (i, j) in visited:
                return False
            if (i >= len(heights) or j >= len(heights[0])):
                return True
            if not (0 <= i < len(heights) and 0 <= j < len(heights[0])):
                return False
            if heights[i][j] > h:
                return False
            visited.add((i, j))
            return (
                checkAtlantic(i + 1, j, heights[i][j], visited) or
                checkAtlantic(i - 1, j, heights[i][j], visited) or
                checkAtlantic(i, j + 1, heights[i][j], visited) or
                checkAtlantic(i, j - 1, heights[i][j], visited)
            )

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if checkPacific(i, j, heights[i][j], set()) and \
                    checkAtlantic(i, j, heights[i][j], set()):
                    res.append([i, j])

        return res