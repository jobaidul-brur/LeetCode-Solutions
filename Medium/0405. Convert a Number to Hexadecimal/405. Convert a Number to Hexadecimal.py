class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        ans = ""
        while num:
            ans += "0123456789abcdef"[num % 16]
            num //= 16
        return ans[::-1]
