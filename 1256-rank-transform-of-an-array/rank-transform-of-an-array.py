class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        s_u = sorted(set(arr))

        r_m = {num: i+1 for i, num in enumerate(s_u)}


        return [r_m[num] for num in arr]