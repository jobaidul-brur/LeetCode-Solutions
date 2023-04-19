class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def missing(n):
            return arr[n] - n - 1

        if missing(0) >= k:
            return k

        lo, hi = 0, len(arr)-1
        while lo < hi:
            mi = (lo + hi + 1) // 2
            if missing(mi) < k:
                lo = mi
            else:
                hi = mi - 1

        return arr[lo]+ k - missing(lo)