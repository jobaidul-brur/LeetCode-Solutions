class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9+7
        dp = [-1] * (high+1)

        def solve(pos):
            if pos > high:
                return 0
            if dp[pos] != -1:
                return dp[pos]
            dp[pos] = (solve(pos+zero) + solve(pos+one)) % mod
            if low <= pos <= high:
                dp[pos] += 1
            return dp[pos]

        return solve(0)
