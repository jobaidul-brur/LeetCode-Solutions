class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, r1, l2, r2):
            res = []
            i, j = l1, l2
            while i <= r1 or j <= r2:
                if i > r1:
                    res.append(nums[j])
                    j += 1
                elif j > r2:
                    res.append(nums[i])
                    i += 1
                elif nums[i] <= nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            nums[l1:r2+1] = res
        
        def merge_sort(l, r):
            if l >= r:
                return
            mid = (l + r) // 2
            merge_sort(l, mid)
            merge_sort(mid+1, r)
            merge(l, mid, mid+1, r)
            
        merge_sort(0, len(nums)-1)
        return nums
