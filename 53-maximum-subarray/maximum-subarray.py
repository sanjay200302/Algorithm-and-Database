
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        def divide(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # Maximum subarray in left half
            left_sum = divide(left, mid)

            # Maximum subarray in right half
            right_sum = divide(mid + 1, right)

            # Maximum subarray crossing the middle
            left_max = float('-inf')
            total = 0

            for i in range(mid, left - 1, -1):
                total += nums[i]
                left_max = max(left_max, total)

            right_max = float('-inf')
            total = 0

            for i in range(mid + 1, right + 1):
                total += nums[i]
                right_max = max(right_max, total)

            cross_sum = left_max + right_max

            return max(left_sum, right_sum, cross_sum)

        return divide(0, len(nums) - 1)
