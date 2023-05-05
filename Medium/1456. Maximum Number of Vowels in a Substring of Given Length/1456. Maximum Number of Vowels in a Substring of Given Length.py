class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        ans = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] in vowels:
                cnt += 1
            if i >= k and s[i-k] in vowels:
                cnt -= 1
            ans = max(ans, cnt)
        return ans
