class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = [1 if x == target else -1 for x in nums]
        ans = 0 
        for i in range (n):
            curr = 0
            for j in range (i,n):
                curr += arr[j]
                if curr > 0:
                    ans += 1
        return ans  