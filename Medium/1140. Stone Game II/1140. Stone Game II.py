class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @lru_cache(None)
        def solve(pos, tern, m):
            if pos == n:
                return 0

            if tern == 1:
                ans = 10**18
                path = -1
                for i in range(pos, min(n, pos+2*m)):
                    if solve(i+1, 0, max(m, i)) < ans:
                        path = i
                    ans = min(ans, solve(i+1, 0, max(m, i+1-pos)))
                # print(f"({pos}, {tern}, {m}) -> ({path+1}, {0}, {max(m, path)})")
                # print(f"pos({pos}), tern({tern}), m({m}), ans({ans})")
                return ans
            else:
                ans = 0
                path = -1
                for i in range(pos, min(n, pos+2*m)):
                    if sum(piles[pos:i+1])+solve(i+1, 1, max(m, i)) > ans:
                        path = i
                    ans = max(ans, sum(piles[pos:i+1])+solve(i+1, 1, max(m, i+1-pos)))
                # print(f"({pos}, {tern}, {m}) -> ({path+1}, {1}, {max(m, path)})")
                # print(f"pos({pos}), tern({tern}), m({m}), ans({ans})")
                return ans

        return solve(0, 0, 1)
