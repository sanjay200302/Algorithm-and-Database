class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0 
        for i in range (n):
            d = set()
            for j in range (i,n):
                d.add(nums[j])
                c = len(d)
                a +=c*c 

        return a  