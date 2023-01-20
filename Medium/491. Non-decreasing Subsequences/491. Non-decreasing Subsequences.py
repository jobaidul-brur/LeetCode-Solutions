class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1, 1 << n):
            tmp = []
            for j in range(n):
                if i & (1 << j):
                    tmp.append(nums[j])
            if len(tmp) >= 2 and tmp == sorted(tmp):
                ans.append(tmp)
        return list(set(map(tuple, ans)))
        
