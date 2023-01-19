class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        
        ans = 0
        s = 0 # sum
        for i in range(len(nums)):
            s = (s + nums[i]) % k
            ans += mp[s]
            mp[s] += 1
        
        return ans
