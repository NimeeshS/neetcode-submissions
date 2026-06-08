class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            class Node:
                def __init__(self):
                    self.children = {}
                    self.is_word = False
            def __init__(self):
                self.root = self.Node()
            def insert(self, word):
                head = self.root
                for ch in word:
                    if ch not in head.children:
                        head.children[ch] = self.Node()
                    head = head.children[ch]
                head.is_word = True
            def search(self, word):
                head = self.root
                for ch in word:
                    if ch not in head.children:
                        return False
                    head = head.children[ch]
                return head.is_word
            def prefix_search(self, prefix):
                head = self.root
                for ch in prefix:
                    if ch not in head.children:
                        return False
                    head = head.children[ch]
                return True
        t = Trie()
        for word in words:
            t.insert(word)

        res = []
        visited = set()

        def dfs(i, j, curr):
            if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return
            if (i, j) in visited:
                return
            curr += board[i][j]
            if not t.prefix_search(curr):
                return
            if t.search(curr):
                res.append(curr)
                root = t.root
                for ch in curr:
                    root = root.children[ch]
                root.is_word = False
            visited.add((i, j))
            dfs(i + 1, j, curr)
            dfs(i - 1, j, curr)
            dfs(i, j + 1, curr)
            dfs(i, j - 1, curr)
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "")

        return res