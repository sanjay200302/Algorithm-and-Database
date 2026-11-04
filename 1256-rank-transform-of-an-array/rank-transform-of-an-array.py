class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rank = {}

        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        return [rank[num] for num in arr]