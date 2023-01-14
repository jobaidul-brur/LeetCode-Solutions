class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        link = [i for i in range(26)]
        
        def find(x):
            if link[x] != x:
                link[x] = find(link[x])
            return link[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            
            if a == b:
                return
            
            if a > b:
                a, b = b, a
            link[b] = a
        
        for i in range(n):
            union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        ans = []
        for c in baseStr:
            ans.append(chr(find(ord(c) - ord('a')) + ord('a')))
        
        return ''.join(ans)
