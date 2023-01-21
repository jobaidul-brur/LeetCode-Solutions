class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        ip = []
        def solve(pos):
            if pos == len(s):
                if len(ip) == 4:
                    res.append('.'.join(ip))
                return
            if len(ip) == 4:
                return
            if s[pos] == '0':
                ip.append('0')
                solve(pos + 1)
                ip.pop()
            else:
                for i in range(pos, len(s)):
                    if int(s[pos:i + 1]) <= 255:
                        ip.append(s[pos:i + 1])
                        solve(i + 1)
                        ip.pop()
        solve(0)
        return res
