class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minKpos = []
        maxKpos = []
        outside_pos = []
        for i in range(0, len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                outside_pos.append(i)
            if nums[i] == minK:
                minKpos.append(i)
            if nums[i] == maxK:
                maxKpos.append(i)
        minKpos.append(len(nums))
        maxKpos.append(len(nums))
        outside_pos.append(len(nums))

        dp = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == minK:
                pos2 = maxKpos[bisect.bisect_left(maxKpos, i)]
                pos3 = outside_pos[bisect.bisect_left(outside_pos, i)]
                if pos3 > pos2:
                    dp[i] = pos3 - pos2
            elif nums[i] == maxK:
                pos2 = minKpos[bisect.bisect_left(minKpos, i)]
                pos3 = outside_pos[bisect.bisect_left(outside_pos, i)]
                if pos3 > pos2:
                    dp[i] = pos3 - pos2
            elif minK < nums[i] < maxK:
                pos2 = min(minKpos[bisect.bisect_left(minKpos, i)], maxKpos[bisect.bisect_left(maxKpos, i)])
                pos3 = outside_pos[bisect.bisect_left(outside_pos, i)]
                if pos3 > pos2:
                    dp[i] = dp[pos2]
        return sum(dp)
