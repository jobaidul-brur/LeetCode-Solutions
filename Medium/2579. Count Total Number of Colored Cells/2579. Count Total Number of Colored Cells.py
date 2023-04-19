class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 5
        a = [1, 4]
        for i in range(2, n):
            a.append(a[-1] + 4)
        return sum(a)
