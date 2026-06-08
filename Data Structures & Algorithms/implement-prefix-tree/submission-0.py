class PrefixTree:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        head = self.root
        for ch in word:
            if ch not in head.children:
                head.children[ch] = self.Node()
            head = head.children[ch]
        head.is_word = True

    def search(self, word: str) -> bool:
        head = self.root
        for ch in word:
            if ch not in head.children:
                return False
            head = head.children[ch]
        return head.is_word

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for ch in prefix:
            if ch not in head.children:
                return False
            head = head.children[ch]
        return True