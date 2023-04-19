class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        negetive = []
        positive = []
        for lev in satisfaction:
            if lev < 0:
                negetive.append(lev)
            else:
                positive.append(lev)

        negetive.sort()
        positive.sort()

        self.ans = 0

        def calc(f, arr):
            res = 0
            for i in range(len(arr)):
                res += (i+f) * arr[i]
            return res

        for i in range(len(negetive) + 1):
            left = calc(1, negetive[i:])
            right = calc(len(negetive[i:]) + 1, positive)
            self.ans = max(self.ans, left + right)

        return self.ans

print(Solution().maxSatisfaction([-2,5,-1,0,3,-3]))