class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        # Step 1: prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + stones[i]

        # Step 2: DP from right to left
        dp = prefix[-1]   # base case: Alice takes all stones
        for i in range(n-2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp   
