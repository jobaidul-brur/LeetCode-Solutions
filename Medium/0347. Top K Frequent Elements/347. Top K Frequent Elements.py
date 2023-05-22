class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                res += bucket[i]
            if len(res) == k:
                return res
        return []
