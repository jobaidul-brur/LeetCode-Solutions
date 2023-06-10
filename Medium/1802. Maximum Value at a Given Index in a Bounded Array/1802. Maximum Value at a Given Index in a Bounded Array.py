class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc(x, n):
            if x == n:
                return x * (x + 1) // 2
            elif x < n:
                return x * (x + 1) // 2 + (n - x)
            else:
                return x * (x + 1) // 2 - (x - n) * (x - n + 1) // 2

        def check(x):
            return calc(x, index + 1) + calc(x, n - index) - x <= maxSum

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
