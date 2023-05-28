class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @lru_cache(None)
        def solve(l, r):
            cnt = 0
            for cut in cuts:
                if l < cut < r:
                    cnt += 1
            if cnt == 0:
                return 0
            
            ans = float('inf')
            for cut in cuts:
                if l < cut < r:
                    ans = min(ans, r - l + solve(l, cut) + solve(cut, r))
            
            return ans
        
        return solve(0, n)
