class Solution:
    def maxProduct(self, n: int) -> int:

        d = sorted(map(int ,str(n)), reverse = True)
        return d[0]*d[1]