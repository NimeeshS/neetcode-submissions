class WordDictionary:
    def __init__(self):
      self.l = []  

    def addWord(self, word: str) -> None:
        self.l.append(word)

    def search(self, word: str) -> bool:
        for i in self.l:
            if len(i) == len(word):
                check = True
                for j in range(len(i)):
                    if i[j] != word[j] and word[j] != ".":
                        check = False
                if check: return True

        return False 
        