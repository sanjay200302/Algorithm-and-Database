class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        m = k
        while True:
            if m not in nums_set:
                return m
            m += k   