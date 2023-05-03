class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans1 = []
        for num in nums1:
            if num not in nums2:
                ans1.append(num)
                
        ans2 = []
        for num in nums2:
            if num not in nums1:
                ans2.append(num)

        return [ans1, ans2]
