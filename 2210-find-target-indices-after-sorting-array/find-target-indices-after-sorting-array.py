class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        a = []
        for i, nums in enumerate(nums):
            if nums == target:
                a.append(i)
        return a 


