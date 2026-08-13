class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        n = len(s)
        for start in range(0,n,2*k):
            i,j = start, min(start+k-1,n-1)
            while i<j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)