class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float('inf')
        best = 0 
        for p in prices:
            best = max(best,p-low)
            low = min(low,p)
        return best 