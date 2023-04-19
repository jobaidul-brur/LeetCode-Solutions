class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: (x[0], x[1]))
        group = 0
        r = -1
        for i in range(len(ranges)):
            if ranges[i][0] > r:
                group += 1
            r = max(r, ranges[i][1])

        def bigmod(a, b, m):
            res = 1
            while b:
                if b & 1:
                    res = (res * a) % m
                a = (a * a) % m
                b >>= 1
            return res

        return bigmod(2, group, 10**9 + 7)