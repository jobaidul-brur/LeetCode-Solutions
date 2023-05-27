class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = -float('inf')
            for j in range(1, 4):
                if i + j <= n:
                    dp[i] = max(dp[i], sum(stoneValue[i:i + j]) - dp[i + j])
        if dp[0] == 0:
            return 'Tie'
        elif dp[0] > 0:
            return 'Alice'
        else:
            return 'Bob'
