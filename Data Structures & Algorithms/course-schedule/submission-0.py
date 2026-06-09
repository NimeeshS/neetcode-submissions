class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for a, b in prerequisites:
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1

            for neighbor in graph.get(node, []):
                if not dfs(neighbor):
                    return False

            state[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True