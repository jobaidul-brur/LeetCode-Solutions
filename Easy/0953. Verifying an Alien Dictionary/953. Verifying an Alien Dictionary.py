class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {c: chr(ord('a') + i) for i, c in enumerate(order)}
        return words == sorted(words, key=lambda w: ''.join(mp[c] for c in w))
