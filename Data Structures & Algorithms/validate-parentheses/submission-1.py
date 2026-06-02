class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in "({[":
                l.append(i)
            else:
                if len(l) == 0: return False
                if i == ")" and l[-1] == "(": l.pop()
                elif i == "]" and l[-1] == "[": l.pop()
                elif i == "}" and l[-1] == "{": l.pop()
                else:
                    return False

        return len(l) == 0