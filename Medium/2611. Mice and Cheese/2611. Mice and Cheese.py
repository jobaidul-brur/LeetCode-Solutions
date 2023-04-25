class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        ans = 0
        sacrifice1 = []
        sacrifice2 = []
        for i in range(n):
            if reward1[i] >= reward2[i]:
                ans += reward1[i]
                sacrifice1.append(reward1[i] - reward2[i])
            else:
                ans += reward2[i]
                sacrifice2.append(reward2[i] - reward1[i])

        sacrifice1.sort()
        sacrifice2.sort()
        if len(sacrifice1) > k:
            ans -= sum(sacrifice1[:len(sacrifice1) - k])
        elif len(sacrifice1) < k:
            ans -= sum(sacrifice2[:k-len(sacrifice1)])

        return ans