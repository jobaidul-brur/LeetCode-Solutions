class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def solve(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
                return 1 + solve(i + 1, j + 1)
            return max(solve(i + 1, j), solve(i, j + 1))

        return solve(0, 0)