from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        arr = []

        # Flatten
        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total

        # Right rotate
        arr = arr[-k:] + arr[:-k]

        # Build answer
        ans = []
        idx = 0

        for _ in range(m):
            ans.append(arr[idx:idx+n])
            idx += n

        return ans