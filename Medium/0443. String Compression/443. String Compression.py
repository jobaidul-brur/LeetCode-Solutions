class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j, n = 0, 0, len(chars)
        ans = 0
        while i < n:
            j = i
            while j+1 < n and chars[i] == chars[j+1]:
                j += 1
            if i == j:
                chars[ans] = chars[i]
                ans += 1
            else:
                s = str(j-i+1)
                chars[ans] = chars[i]
                chars[ans+1: ans+1+len(s)] = s
                ans += 1 + len(s)

            i = j + 1
        
        return ans
