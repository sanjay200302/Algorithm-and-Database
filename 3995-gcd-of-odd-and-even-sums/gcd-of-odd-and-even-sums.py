class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        so = n*n
        se = n*(n+1)
        return gcd(so,se)
        