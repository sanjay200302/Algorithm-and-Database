class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for key, _ in groupby(nums):
            nums[k]= key
            k += 1


        return k 
        