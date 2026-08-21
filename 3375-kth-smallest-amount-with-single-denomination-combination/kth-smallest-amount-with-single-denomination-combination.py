class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Custom gcd for compatibility
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def count(x: int) -> int:
            total = 0
            m = len(coins)
            for mask in range(1, 1 << m):
                lcm = 1
                bits = 0
                for i in range(m):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm * coins[i] // gcd(lcm, coins[i])
                        if lcm > x:
                            break
                else:
                    if bits % 2 == 1:
                        total += x // lcm
                    else:
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
