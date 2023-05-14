class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (1 << n)

        def solve(mask):
            if mask == 0:
                return 0
            if dp[mask] != -1:
                return dp[mask]
            ans = 0
            for i in range(n):
                if mask & (1 << i):
                    for j in range(i + 1, n):
                        if mask & (1 << j):
                            ans = max(ans, solve(mask ^ (1 << i) ^ (1 << j)) +
                                      gcd(nums[i], nums[j]) * ((n - bin(mask).count('1')) // 2 + 1))
            dp[mask] = ans
            return ans

        return solve((1 << n) - 1)

