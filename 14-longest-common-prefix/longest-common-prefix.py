class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""
        
        s = min(strs)
        l = max(strs)


        for i in range (len(s)):
            if s[i] != l[i]:
                return s [:i]
        return s
        