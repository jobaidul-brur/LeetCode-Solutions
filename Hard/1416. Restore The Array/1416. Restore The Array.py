class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            for j in range(i, n):
                if int(s[i:j + 1]) > k:
                    break
                dp[i] += dp[j + 1]
                dp[i] %= 1000000007
        return dp[0]
