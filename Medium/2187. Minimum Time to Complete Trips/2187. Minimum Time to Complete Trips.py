class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(k):
            return sum(k//t for t in time) >= totalTrips

        ans = -1
        lo, hi = 1, 10 ** 15
        while lo <= hi:
            mid = (lo+hi)//2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans