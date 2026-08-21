class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Custom gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Precompute all subset LCMs
        subset_lcms = []
        m = len(coins)

        def dfs(i, lcm, bits):
            if i == m:
                if bits > 0:
                    subset_lcms.append((lcm, bits % 2))  # (lcm, parity)
                return
            # skip coin[i]
            dfs(i + 1, lcm, bits)
            # include coin[i]
            new_lcm = lcm * coins[i] // gcd(lcm, coins[i])
            dfs(i + 1, new_lcm, bits + 1)

        dfs(0, 1, 0)

        def count(x: int) -> int:
            total = 0
            for lcm, parity in subset_lcms:
                if lcm > x:
                    continue
                if parity == 1:  # odd subset size → add
                    total += x // lcm
                else:            # even subset size → subtract
                    total -= x // lcm
            return total

        lo, hi = min(coins), k * min(coins)
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
