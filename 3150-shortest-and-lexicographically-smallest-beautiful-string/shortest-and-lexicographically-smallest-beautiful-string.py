class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        min_len = float("inf")

        # Sliding window
        left = 0
        ones = 0
        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Shrink window if too many ones
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # If exactly k ones, check substring
            if ones == k:
                while left <= right and s[left] == '0':
                    left += 1  # trim leading zeros
                length = right - left + 1
                substring = s[left:right+1]

                if length < min_len or (length == min_len and substring < res):
                    min_len = length
                    res = substring

        return res