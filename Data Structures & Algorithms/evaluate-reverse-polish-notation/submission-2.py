class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        for i in tokens:
            if i == "+":
                l.append(l.pop() + l.pop())
            elif i == "-":
                l.append(-l.pop() + l.pop())
            elif i == "*":
                l.append(l.pop() * l.pop())
            elif i == "/":
                denom = l.pop()
                num = l.pop()
                l.append(int(num / denom))
            else:
                l.append(int(i))

        return l.pop()