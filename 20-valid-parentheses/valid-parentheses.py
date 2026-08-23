class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        ma = {')': '(', '}': '{', ']': '['}  
        for char in s:
            if char in ma:
                t_p = st.pop() if st else "#"
                if ma[char] != t_p:
                    return False
            else:
                st.append(char)
        return not st 