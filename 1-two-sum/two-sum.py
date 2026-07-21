class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i , nums in enumerate(nums):
            c = target - nums
            if c in seen:
                return[seen[c],i]
            seen[nums]= i