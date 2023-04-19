class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        @lru_cache(None)
        def solve(l1, r1, l2, r2):
            if r1 - l1 != r2 - l2:
                return False
            if r1 - l1 == 1:
                return s1[l1] == s2[l2]
            if s1[l1:r1] == s2[l2:r2]:
                return True
            for i in range(1, r1-l1):
                if solve(l1, l1+i, l2, l2+i) and solve(l1+i, r1, l2+i, r2):
                    return True
                if solve(l1, l1+i, r2-i, r2) and solve(l1+i, r1, l2, r2-i):
                    return True
            return False
        return solve(0, n, 0, n)