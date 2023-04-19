class Solution:
    def splitNum(self, num: int) -> int:
        a = list(str(num))
        a.sort()
        l = []
        r = []
        i = 0
        while i < len(a):
            l.append(a[i])
            i += 1
            if i < len(a):
                r.append(a[i])
                i += 1
        return int(''.join(l)) + int(''.join(r))
            
