class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        n = len(candies)
        ans = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                ans[i] = True

        return ans