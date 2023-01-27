class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isWord = False

        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isWord = True

        ans = []

        for word in words:
            # print("word: ", word)
            n = len(word)
            dp = [-1] * (n)
            def solve(i):
                if i == n:
                    return 1
                if dp[i] != -1:
                    return dp[i]
                node = root
                for j in range(i, n):
                    if word[j] not in node.children:
                        break
                    node = node.children[word[j]]
                    if node.isWord:
                        if i == 0 and j == n - 1:
                            continue
                        if solve(j + 1) == 1:
                            dp[i] = 1
                            return dp[i]
                dp[i] = 0
                return dp[i]

            if solve(0) == 1:
                ans.append(word)

        return ans
