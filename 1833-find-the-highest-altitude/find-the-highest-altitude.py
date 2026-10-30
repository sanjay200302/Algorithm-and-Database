class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        c = 0
        h = 0
        for g in gain:
            c += g
            h = max(h,c)  
        

        return h