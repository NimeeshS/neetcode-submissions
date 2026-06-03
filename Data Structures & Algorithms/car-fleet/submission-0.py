class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        l = []
        for i in cars:
            time = (target - i[0]) / i[1]
            if l and time <= l[-1]:
                continue
            else:
                l.append(time)

        return len(l)