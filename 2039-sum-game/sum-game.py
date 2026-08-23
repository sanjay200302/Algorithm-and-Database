class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        sum1 = sum(int(c) for c in num[:half] if c != '?')
        sum2 = sum(int(c) for c in num[half:] if c != '?')

        q1 = num[:half].count('?')
        q2 = num[half:].count('?')

        # If odd number of '?' → Alice wins
        if (q1 + q2) % 2 == 1:
            return True

        # Check balance condition
        diff = sum1 - sum2
        return diff != (q2 - q1) * 9 // 2