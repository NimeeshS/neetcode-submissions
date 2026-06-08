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

    def _rsearch(self, word, node):
        if not word:
            return node.is_word
        if word[0] == ".":
            for child in node.children:
                if self._rsearch(word[1:], node.children[child]):
                    return True
            return False
        else:
            if word[0] not in node.children:
                return False
            return self._rsearch(word[1:], node.children[word[0]])

    def search(self, word: str) -> bool:
        return self._rsearch(word, self.root)