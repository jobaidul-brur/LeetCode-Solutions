class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i >= j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = solve(i + 1, j - 1)
            else:
                dp[i][j] = min(solve(i + 1, j), solve(i, j - 1)) + 1
            return dp[i][j]

        return solve(0, n - 1)