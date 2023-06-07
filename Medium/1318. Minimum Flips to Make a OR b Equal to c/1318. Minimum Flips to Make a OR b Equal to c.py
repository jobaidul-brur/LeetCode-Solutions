class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aORb = a | b
        aANDb = a & b
        ans = bin(aORb ^ c).count('1')
        ans += bin(aANDb & (~c)).count('1')

        return ans
