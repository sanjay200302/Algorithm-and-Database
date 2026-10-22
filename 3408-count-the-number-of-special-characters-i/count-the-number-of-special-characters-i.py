class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = set(word)
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in c and ch.upper() in c:
                count += 1 
        return count  

        