class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = 0
        for i in range(1, min(len(str1), len(str2)) + 1):
            if str1[:i] == str2[:i] and str1[:i] * (len(str1) // i) == str1 and str2[:i] * (len(str2) // i) == str2:
                ans = i
        
        return str1[:ans]
