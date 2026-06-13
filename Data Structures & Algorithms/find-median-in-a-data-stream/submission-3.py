class MedianFinder:
    def __init__(self):
       self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()

    def findMedian(self) -> float:
        n = len(self.l)
        if n % 2 == 0:
            return (self.l[n // 2] + self.l[(n // 2) - 1]) / 2
        else:
            return self.l[n // 2]