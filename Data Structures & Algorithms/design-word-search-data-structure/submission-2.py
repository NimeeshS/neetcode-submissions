class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        head = self.root
        for ch in word:
            if ch not in head.children:
                head.children[ch] = self.Node()
            head = head.children[ch]
        head.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_word
            if word[i] == ".":
                for child in node.children:
                    if dfs(i + 1, node.children[child]):
                        return True
                return False
            if word[i] not in node.children:
                return False
            return dfs(i + 1, node.children[word[i]])
        return dfs(0, self.root)