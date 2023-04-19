class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append(-1)
        prev = 1
        cnt = 0
        ans = 0
        for num in nums:
            if num == 0:
                if prev == 0:
                    cnt += 1
                else:
                    cnt = 1
            else:
                ans += cnt*(cnt+1)//2
                cnt = 0

            prev = num

        return ans