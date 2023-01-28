from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.maxn = 10**4+10
        self.left = [self.maxn + 1] * self.maxn
        self.right = [-1] * self.maxn
        self.st = SortedSet()

    def addNum(self, value: int) -> None:
        if self.right[value] != -1:
            return
        self.left[value] = self.left[value - 1] if value > 0 and self.right[value - 1] != -1 else value
        self.right[value] = self.right[value + 1] if self.right[value + 1] != -1 else value
        self.left[self.right[value]] = self.left[value]
        self.right[self.left[value]] = self.right[value]
        self.st.add(value);

    def getIntervals(self) -> List[List[int]]:
        x = -1
        ans = []
        while True:
            x = self.st.bisect_right(x)
            if x == len(self.st):
                break
            x = self.st[x]
            ans.append([self.left[x], self.right[x]])
            x = self.right[x]

        return ans




# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
