class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * len(days)
        dp[-1] = min(costs)
        for i in range(len(days) - 2, -1, -1):
            dp[i] = dp[i + 1] + costs[0]
            for j in range(i + 1, len(days)):
                if days[j] - days[i] > 6:
                    dp[i] = min(dp[i], dp[j] + costs[1])
                    break
            if days[-1] - days[i] <= 6:
                dp[i] = min(dp[i], costs[1])
            for j in range(i + 1, len(days)):
                if days[j] - days[i] > 29:
                    dp[i] = min(dp[i], dp[j] + costs[2])
                    break
            if days[-1] - days[i] <= 29:
                dp[i] = min(dp[i], costs[2])

        return dp[0]