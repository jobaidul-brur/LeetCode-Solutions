class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = zip(nums1, nums2)
        nums = sorted(nums, key=lambda x: x[1], reverse=True)

        min_heap = []
        sum = 0
        for i in range(k):
            heapq.heappush(min_heap, nums[i][0])
            sum += nums[i][0]

        ans = nums[k-1][1] * sum
        for i in range(k, len(nums)):
            top = heapq.heappop(min_heap)
            sum -= top

            sum += max(nums[i][0], top)
            heapq.heappush(min_heap, max(nums[i][0], top))

            ans = max(ans, nums[i][1] * sum)

        return ans