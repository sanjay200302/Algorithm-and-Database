class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = defaultdict(int)         
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            unique_in_window = set(window) 
            for num in unique_in_window:
                count[num] += 1   
        
        candidates = [num for num, c in count.items() if c == 1]
        
        return max(candidates) if candidates else -1